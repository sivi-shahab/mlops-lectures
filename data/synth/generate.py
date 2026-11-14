"""Synthetic fraud + credit data with drift, delayed labels, fraud rings and reject bias.

All PII columns are random fakes for privacy exercises (Module 12).
Usage: python data/synth/generate.py --out data/synth --seed 42
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

CATEGORIES = ["grocery", "fuel", "ecommerce", "travel", "electronics", "restaurant"]
RISKY = {"ecommerce", "electronics", "crypto_exchange"}
REGIONS = ["DKI Jakarta", "Jawa Barat", "Jawa Timur", "Sumatera Utara", "Bali", "Sulawesi Selatan"]


def _times(n, start, months, rng):
    span = pd.Timedelta(days=30 * months).total_seconds()
    return pd.Timestamp(start) + pd.to_timedelta(np.sort(rng.uniform(0, span, n)), unit="s")


def _digits(n, k, rng):
    return ["".join(map(str, row)) for row in rng.integers(0, 10, size=(n, k))]


def fraud(n, start, months, drift_start, rng):
    n_cards = max(n // 40, 50)
    home_device = rng.integers(0, n_cards * 2, n_cards)
    t = _times(n, start, months, rng)
    post = np.asarray(t >= pd.Timestamp(drift_start))

    card = rng.integers(0, n_cards, n)
    new_device = rng.random(n) < 0.05
    device = np.where(new_device, rng.integers(0, n_cards * 2, n), home_device[card])

    cats = np.array(CATEGORIES + ["crypto_exchange"])
    p_pre = np.array([0.3, 0.15, 0.25, 0.05, 0.1, 0.15, 0.0])
    p_post = np.array([0.25, 0.12, 0.25, 0.05, 0.1, 0.13, 0.10])
    category = np.where(post, rng.choice(cats, n, p=p_post), rng.choice(cats, n, p=p_pre))

    amount = rng.lognormal(np.log(150_000), 1.0, n) * np.where(post, 1.6, 1.0)
    os_ = np.where(rng.random(n) < np.where(post, 0.75, 0.55), "android", "ios")

    z = (np.log(amount) - np.log(150_000)) + 1.5 * new_device + 1.0 * np.isin(category, list(RISKY))
    is_fraud = rng.random(n) < 1 / (1 + np.exp(-(z - 7.2)))

    df = pd.DataFrame({
        "event_time": t, "card_id": card, "device_id": device, "merchant_category": category,
        "region": rng.choice(REGIONS, n), "device_os": os_, "amount": amount.round(0), "is_fraud": is_fraud,
    })

    # Fraud ring: 50 cards sharing 5 devices, bursts of escalating amounts after drift_start (adversarial pattern).
    n_ring = max(n // 1000, 50)
    ring_cards = rng.choice(n_cards, 50, replace=False)
    ring_start = pd.Timestamp(drift_start)
    ring = pd.DataFrame({
        "event_time": ring_start + pd.to_timedelta(np.sort(rng.uniform(0, 30 * 86400, n_ring)), unit="s"),
        "card_id": rng.choice(ring_cards, n_ring),
        "device_id": rng.choice(np.arange(10**7, 10**7 + 5), n_ring),
        "merchant_category": rng.choice(["ecommerce", "crypto_exchange"], n_ring),
        "region": "DKI Jakarta", "device_os": "android",
        "amount": (rng.lognormal(np.log(50_000), 0.3, n_ring) * np.linspace(1, 40, n_ring)).round(0),
        "is_fraud": True,
    })
    df = pd.concat([df, ring], ignore_index=True).sort_values("event_time", ignore_index=True)

    m = len(df)
    df.insert(0, "tx_id", np.arange(m))
    df["merchant_id"] = rng.integers(0, 2000, m)
    df["is_fraud"] = df["is_fraud"].astype(int)
    # Delayed labels: chargeback confirmed 30-90 days after the transaction.
    df["label_available_at"] = df["event_time"] + pd.to_timedelta(rng.uniform(30, 90, m), unit="D")
    card_numbers = np.array(_digits(n_cards, 16, rng))
    df["card_number"] = card_numbers[df["card_id"]]
    df["customer_name"] = "Customer " + df["card_id"].astype(str)
    df["phone"] = ["08" + d for d in _digits(m, 10, rng)]
    return df


def credit(n, start, months, drift_start, rng):
    t = _times(n, start, months, rng)
    post = np.asarray(t >= pd.Timestamp(drift_start))

    age = rng.integers(21, 66, n)
    income = rng.lognormal(np.log(8_000_000), 0.5, n) * np.where(post, 0.85, 1.0)
    dti = np.clip(rng.beta(2, 5, n) + np.where(post, 0.08, 0.0), 0, 1.5)
    utilization = rng.beta(2, 3, n)
    months_oldest = rng.integers(0, 240, n)
    n_delinq = rng.poisson(0.3 + 0.5 * dti)

    logit = (-3.0 + 2.5 * dti + 1.5 * utilization + 0.5 * n_delinq
             - 0.6 * np.log(income / 8_000_000) - 0.004 * months_oldest - 0.01 * (age - 40))
    pd_true = 1 / (1 + np.exp(-logit))
    default = (rng.random(n) < pd_true).astype(float)

    # Bank policy approves ~70 % using a noisy view of risk -> outcomes only observed for approved (reject bias).
    policy_score = logit + rng.normal(0, 0.5, n)
    approved = policy_score < np.quantile(policy_score, 0.7)
    default[~approved] = np.nan

    return pd.DataFrame({
        "app_id": np.arange(n), "application_date": t, "vintage": t.strftime("%Y-%m"),
        "performance_end": t + pd.DateOffset(months=12),
        "age": age, "income": income.round(-3), "dti": dti.round(4), "utilization": utilization.round(4),
        "months_oldest_account": months_oldest, "n_delinquencies": n_delinq,
        "region": rng.choice(REGIONS, n), "gender": rng.choice(["F", "M"], n),
        "nik": _digits(n, 16, rng), "full_name": ["Applicant " + str(i) for i in range(n)],
        "is_approved": approved.astype(int), "default_12m": default,
    })


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", default="data/synth")
    p.add_argument("--n-tx", type=int, default=200_000)
    p.add_argument("--n-apps", type=int, default=50_000)
    p.add_argument("--start", default="2025-01-01")
    p.add_argument("--months", type=int, default=18)
    p.add_argument("--drift-start", default="2026-01-01")
    p.add_argument("--seed", type=int, default=42)
    a = p.parse_args(argv)

    rng = np.random.default_rng(a.seed)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    f = fraud(a.n_tx, a.start, a.months, a.drift_start, rng)
    c = credit(a.n_apps, a.start, a.months, a.drift_start, rng)
    f.to_parquet(out / "fraud_transactions.parquet", index=False)
    c.to_parquet(out / "credit_applications.parquet", index=False)
    print(f"fraud: {len(f)} rows, fraud rate {f.is_fraud.mean():.4f}")
    print(f"credit: {len(c)} rows, approval {c.is_approved.mean():.3f}, bad rate (approved) {c.default_12m.mean():.3f}")
    return f, c


if __name__ == "__main__":
    main()
