# When breakeven: average price * total coins = total costs
# <=> average price = total costs / total coins

def coins(cost: float, price: float) -> float:
    return cost/price

class dca:
    def __init__(self, p_list: list[dict]) -> None:
        # dict follows rule: {cost: float, price: float}
        self.p_list = p_list

    def breakeven(self) -> float:
        total_cost = 0
        total_coins = 0

        for pos in self.p_list:
            total_cost += list(pos.values())[0]
            total_coins += coins(*list(pos.values()))

        return total_cost / total_coins

if __name__ == "__main__":
    postions_list = [{"cost": 200, "price": 15.048},
    {"cost": 200, "price": 14.212},
    {"cost": 200, "price": 14.010},
    {"cost": 200, "price": 13.733},
    {"cost": 200, "price": 13.372}]

    be=dca(postions_list).breakeven()
    print(be)