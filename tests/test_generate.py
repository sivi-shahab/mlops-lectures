"""Self-check for the synthetic generator. Run: python tests/test_generate.py (or pytest)."""
import sys
import tempfile
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "data" / "synth"))
from generate import main  # noqa: E402


def test_generator():
    with tempfile.TemporaryDirectory() as d:
        f, c = main(["--out", d, "--n-tx", "100000", "--n-apps", "20000", "--seed", "1"])
    drift = pd.Timestamp("2026-01-01")

    # Fraud: imbalance, delayed labels, drift, fraud ring
    assert 0.002 < f.is_fraud.mean() < 0.03, f.is_fraud.mean()
    delay = (f.label_available_at - f.event_time).dt.days
    assert delay.between(29, 90).all()
    pre, post = f[f.event_time < drift], f[f.event_time >= drift]
    assert post.amount.median() / pre.amount.median() > 1.3
    assert "crypto_exchange" not in set(pre.merchant_category)
    assert f.groupby("device_id").card_id.nunique().max() >= 5  # shared ring devices
    assert f.card_number.str.fullmatch(r"\d{16}").all()

    # Credit: reject bias, plausible bad rate, drift
    assert c.loc[c.is_approved == 0, "default_12m"].isna().all()
    assert c.loc[c.is_approved == 1, "default_12m"].notna().all()
    assert 0.65 < c.is_approved.mean() < 0.75
    assert 0.02 < c.default_12m.mean() < 0.25, c.default_12m.mean()
    cpre, cpost = c[c.application_date < drift], c[c.application_date >= drift]
    assert cpost.dti.mean() > cpre.dti.mean() + 0.05


if __name__ == "__main__":
    test_generator()
    print("ok")
