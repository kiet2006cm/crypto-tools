# assume that we know the leverage and the breakeven, and the leverage fees = 0
# liq occurs when the price drop bellow the breakeven breakeven/leverage
# so the liq price is breakeven - breakeven/leverage

def liq(breakeven: float, leverage: int) -> float:
    return breakeven * (1 - 1/leverage)

if __name__ == "__main__":
    breakeven = 14.053032009798878
    leverage = 2

    liq_price = liq(breakeven, leverage)
    print(liq_price)