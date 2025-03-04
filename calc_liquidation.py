def calculate_liquidation_price(breakeven_price, leverage, position_type):
    """
    Calculate the liquidation price for a long or short position.
    
    :param breakeven_price: The breakeven price of the position.
    :param leverage: The leverage used for the trade.
    :param position_type: "long" or "short" position.
    :return: The liquidation price.
    """
    
    if leverage <= 1:
        raise ValueError("Leverage must be greater than 1.")
    
    maintenance_margin = 0.005  # Typically 0.5% (can vary by exchange)
    
    if position_type.lower() == "long":
        liquidation_price = breakeven_price * (1 - (1 / leverage) + maintenance_margin)
    elif position_type.lower() == "short":
        liquidation_price = breakeven_price * (1 + (1 / leverage) - maintenance_margin)
    else:
        raise ValueError("Position type must be 'long' or 'short'.")
    
    return liquidation_price

# Example usage
if __name__ == "__main__":
    breakeven_price = float(input("Enter breakeven price: "))
    leverage = float(input("Enter leverage: "))
    position_type = input("Enter position type (long/short): ")
    
    try:
        liquidation_price = calculate_liquidation_price(breakeven_price, leverage, position_type)
        print(f"Liquidation Price for {position_type} position: {liquidation_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
