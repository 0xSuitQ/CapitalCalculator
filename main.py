"""

"""

def find_capital(n, c, gains, prices):
    if memo[n][c] != None:
        return memo[n][c]
    if n == 0 or c == 0:
        result = 0
    elif prices[n-1] > c:
        result = find_capital(n-1, c, gains, prices)
    else:
        tmp1 = find_capital(n-1, c, gains, prices)
        tmp2 = gains[n-1] + find_capital(n-1, c-prices[n-1], gains, prices)
        result = max(tmp1, tmp2)
    memo[n][c] = result
    return result


while (True):
    n = int(input("Enter the maximum amount of laptops: "))
    c = int(input("Enter the capital: "))
    gains = list(map(int, input("Enter the gains array separated by space: ").split()))
    prices = list(map(int, input("Enter the prices array separated by space: ").split()))
    memo = [[None] * (c + 1) for _ in range(n + 1)]
    capital = find_capital(n, c, gains, prices)
    print("Maximum capital at the end of summer:", capital)
    if (input("Do you want to run the program again? (y/n): ").lower() != 'y'):
        break
