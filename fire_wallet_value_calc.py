"""
FIRE wallet value calculator.

Computes the portfolio ("wallet") value needed so that a fixed real (inflation-adjusted)
monthly withdrawal can be sustained indefinitely, without depleting principal in real terms.

Key idea:
    The original version divided by the *nominal* monthly growth rate. That only works if
    prices never rise. In reality, if your portfolio grows 0.5%/month but inflation is
    0.2%/month, your purchasing power only grows ~0.3%/month. Using the nominal rate
    understates the wallet value you actually need to keep up with inflation forever.

    This version converts the nominal monthly growth rate into a *real* monthly growth
    rate (Fisher equation) and uses that for the perpetuity calculation:

        real_rate = (1 + nominal_monthly_rate) / (1 + monthly_inflation_rate) - 1
        wallet_value = sell_month / real_rate

    This is the classic "perpetual withdrawal" formula: if the real rate of return exactly
    equals what you withdraw as a fraction of the portfolio, the portfolio's real value
    (and thus your real withdrawal) stays constant forever.

Usage:
    python fire_wallet_value_calc.py \
        --growth-rate 0.005 \
        --inflation-rate 0.002 \
        --withdrawal 3000 \
        --tax 0.22 \
        [--annual]

Arguments can be given as monthly rates (default) or annual rates (--annual flag),
in which case they are converted to monthly automatically.
"""

import argparse
import sys


def annual_to_monthly(annual_rate: float) -> float:
    """Convert an annual rate to an equivalent monthly compounding rate."""
    return (1 + annual_rate) ** (1 / 12) - 1


def compute_real_monthly_rate(nominal_monthly_rate: float, monthly_inflation_rate: float) -> float:
    """Fisher equation: real rate net of inflation, both expressed monthly."""
    return (1 + nominal_monthly_rate) / (1 + monthly_inflation_rate) - 1


def compute_wallet_value(monthly_withdrawal: float, tax: float, real_monthly_rate: float):
    """
    Returns (sell_month, wallet_value).

    sell_month:    gross amount you must sell each month to net `monthly_withdrawal`
                    after capital gains tax.
    wallet_value:  portfolio size such that the real monthly return alone funds
                    sell_month forever, preserving purchasing power.
    """
    if tax >= 1:
        raise ValueError("tax must be less than 1 (e.g. 0.22 for 22%)")
    sell_month = monthly_withdrawal / (1 - tax)

    if real_monthly_rate <= 0:
        raise ValueError(
            "Real monthly rate is <= 0 (your growth rate does not outpace inflation). "
            "A finite wallet value cannot sustain withdrawals forever at this rate."
        )
    wallet_value = sell_month / real_monthly_rate
    return sell_month, wallet_value


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Compute the wallet value needed to sustain a real (inflation-adjusted) "
                    "monthly withdrawal forever."
    )
    parser.add_argument(
        "--growth-rate", type=float, required=True,
        help="Nominal portfolio growth rate as a decimal (e.g. 0.005 for 0.5%%). "
            "Monthly by default, or annual if --annual is passed.",
    )
    parser.add_argument(
        "--inflation-rate", type=float, required=True,
        help="Inflation rate as a decimal (e.g. 0.002 for 0.2%%). "
            "Monthly by default, or annual if --annual is passed.",
    )
    parser.add_argument(
        "--withdrawal", type=float, required=True,
        help="Desired net monthly withdrawal amount, in today's purchasing power.",
    )
    parser.add_argument(
        "--tax", type=float, required=True,
        help="Capital gains tax rate as a decimal (e.g. 0.22 for 22%%).",
    )
    parser.add_argument(
        "--annual", action="store_true",
        help="Treat --growth-rate and --inflation-rate as annual rates and convert them to monthly.",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    nominal_monthly_rate = args.growth_rate
    monthly_inflation_rate = args.inflation_rate
    if args.annual:
        nominal_monthly_rate = annual_to_monthly(args.growth_rate)
        monthly_inflation_rate = annual_to_monthly(args.inflation_rate)
        print(f"Converted annual growth rate {args.growth_rate:.4%} -> monthly {nominal_monthly_rate:.4%}")
        print(f"Converted annual inflation rate {args.inflation_rate:.4%} -> monthly {monthly_inflation_rate:.4%}")

    real_monthly_rate = compute_real_monthly_rate(nominal_monthly_rate, monthly_inflation_rate)
    print(f"Real monthly rate (net of inflation): {real_monthly_rate:.4%}")

    try:
        sell_month, wallet_value = compute_wallet_value(args.withdrawal, args.tax, real_monthly_rate)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"sell_month: {sell_month:.2f}")
    print(f"wallet value to sustain {args.withdrawal:.2f}/month (real terms) forever: {wallet_value:.2f}")


if __name__ == "__main__":
    main()
