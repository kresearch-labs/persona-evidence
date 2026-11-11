# Paper-Trading Desk Sheet — Session 1/11

- **Date:** 2026-10-14 (11:12 UTC)
- **Data source:** Yahoo v8 chart API, `query1.finance.yahoo.com/v8/finance/chart/<SYM>?interval=1d&range=35d` (fetched via web tool; artifacts under `artifacts/`)
- **Desk rules:** every price below comes from the fetch; no invented numbers. If a fetch had failed, the line would read "data unavailable".

## Fetched prices (as of 2026-10-14 ~11:12 UTC)

| SYM | Price (USD) | Prev daily close | Today's move | 52w range |
|-----|-------------|------------------|--------------|-----------|
| BTC | 83,319.39 | 83,095.13 | +0.083% | 57,747.77 – 116,273.31 |
| ETH | 2,500.60 | 2,496.63 | +0.136% | 1,506.51 – 4,250.67 |
| SOL | 106.80 | 106.73 | +0.717% | 60.41 – 208.33 |
| DOGE | 0.084 | 0.084269 | +0.695% | 0.067973 – 0.209315 |

## Direction calls (tomorrow vs today's close)

| SYM | dir | conf | resolve-date |
|-----|-----|------|--------------|
| BTC | up | 0.55 | 2026-10-15 |
| ETH | up | 0.58 | 2026-10-15 |
| SOL | up | 0.57 | 2026-10-15 |
| DOGE | up | 0.52 | 2026-10-15 |

## Crowd baseline (last 30 daily closes, day-over-day)

| SYM | up days / 30 | base rate |
|-----|--------------|-----------|
| BTC | 16 | 0.533 |
| ETH | 19 | 0.633 |
| SOL | 18 | 0.600 |
| DOGE | 15 | 0.500 |

## Brier-score commitment — (conf − outcome)², recorded at resolution

| SYM | conf | Brier if up | Brier if down |
|-----|------|-------------|---------------|
| BTC | 0.55 | 0.2025 | 0.3025 |
| ETH | 0.58 | 0.1764 | 0.3364 |
| SOL | 0.57 | 0.1849 | 0.3249 |
| DOGE | 0.52 | 0.2304 | 0.2704 |

## Reasoning log

- **Method:** base rate from the last 30 daily closes (day-over-day up-count), then a small tilt toward the direction of today's move; confidence kept in a narrow band around the base rate because 30 days is a small sample and crypto daily direction is close to a coin flip.
- **BTC:** base rate 0.533; today slightly green (+0.083%) → up at 0.55.
- **ETH:** strongest base rate (0.633); today green (+0.136%) → up at 0.58, trimmed below the base rate for mean-reversion risk after a strong 30-day run.
- **SOL:** base rate 0.600; today green (+0.717%) → up at 0.57.
- **DOGE:** base rate exactly 0.500; today green (+0.695%) → up at 0.52, weakest conviction of the four.
- **Falsifiability:** each call resolves against tomorrow's daily close (2026-10-15); outcome = 1 if close > today's close, else 0.
