

# Task
# Imagine you are a student who makes money by buying, fixing, 
# and selling laptops. You want to increase your capital this summer.
# As summer has a limited amount of time, you could only buy, fix, 
# and resell a limited number of laptops, let’s say “N” distinct laptops.
# You need to increase your capital as much as possible.

# You have “K” laptops, with laptop index “i”. You expect gains “gains[i]” 
# for the laptop, the price of the laptop which would be “price[i]”. 
# Initially, you would have a “C” amount of capital. When summer finishes, you will have profit, which will be added to your capital. 

# You need to collect a list of at most “N” laptops you would buy to maximise your income. As a result, output the capital size that you would have after summer ends.
# Result
# As a result, you should have a CLI application that receives inputs
# “N”, “C”, “gains array”, “price array” and output “capital at the end of the summer”.
# Please include instructions on how to run the application in README.md.



n = int(input("Enter the maximum amount of laptops: ")) 
c = int(input("Enter the capital: "))
gains = list(map(int, input("Enter the gains array separated by space: ").split()))
prices = list(map(int, input("Enter the prices array separated by space: ").split()))

memo = [[None] * (c + 1) for _ in range(n + 1)]

# print(array)
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
	

capital = find_capital(n, c, gains, prices)
print("Maximum capital at the end of summer:", capital)
