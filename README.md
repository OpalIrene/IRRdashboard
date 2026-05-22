# IRR Dashboard

A starter Streamlit dashboard for reviewing a bank's balance-sheet interest rate risk (IRR) position using UBPR-style data.

## Purpose

This tool is designed to help evaluate whether a bank appears more asset sensitive or liability sensitive based on repricing exposure, earning assets, funding mix, and assumed rate movements.

## Current Features

- Loads sample UBPR-style balance sheet data
- Calculates rate-sensitive assets (RSA)
- Calculates rate-sensitive liabilities (RSL)
- Computes a simple GAP ratio
- Estimates directional net interest income exposure
- Displays dashboard metrics and charts

## Planned Features

- FFIEC UBPR import support
- Call report integration
- Economic Value of Equity (EVE) analysis
- Deposit beta assumptions
- Peer bank comparisons
- Stress testing scenarios
- Examiner-style write-up generation

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Disclaimer

This dashboard is for educational and analytical purposes only and is not a substitute for formal ALM or IRR modeling.
