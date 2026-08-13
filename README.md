# Wallet Ledger

A small pair of inflation-aware FIRE calculators, hosted with GitHub Pages.

**Live site:** https://ferocemarcello.github.io/investments/

- **[Spend it](https://ferocemarcello.github.io/investments/index.html)** — wallet value calculator. Given a growth rate, inflation rate, monthly/annual withdrawal, and capital gains tax, computes the portfolio value needed to sustain that withdrawal forever in today's purchasing power.
- **[Grow it](https://ferocemarcello.github.io/investments/portfolio.html)** — portfolio growth calculator. Given a starting balance, a monthly/annual contribution, a growth rate, and a number of years, projects the future portfolio value.

## Files

- `index.html` — the "Spend it" wallet value calculator (the website's root/home page)
- `portfolio.html` — the "Grow it" portfolio growth calculator
- `fire_wallet_value_calc.py` — command-line version of the wallet value calculation, matching the math used by `index.html`

## Math

Both pages convert between monthly and annual rates using standard compounding:

```
annual = (1 + monthly)^12 - 1
monthly = (1 + annual)^(1/12) - 1
```

The wallet value calculator additionally divides by the *real* rate of return — nominal growth net of inflation — so the sustainable withdrawal keeps its purchasing power indefinitely, rather than eroding over time.
