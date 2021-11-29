def maximize_profit(price):
    i = 0
    n = len(price)
    if n == 1:
        return
    while i < n - 1:
        while (i < n-1) and price[i+1] <= price[i]:
            i += 1

        if i == n-1:
            break

        buy = i
        i += 1

        while (i < n) and price[i] >= price[i-1]:
            i += 1

        sell = i - 1

        print("Buy: ", buy)
        print("Sell: ", sell)


price = [100, 180, 260, 310, 40, 535, 695]
maximize_profit(price)
