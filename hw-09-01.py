import time

# Алгоритм жадібного програмування
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        count = amount // coin
        if count:
            result[coin] = count
            amount %= coin
    return result

# Алгоритм динамічного програмування
def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    change = {}
    i = amount
    for coin in reversed(coins):
        change[coin] = i // coin
        i %= coin

    return change

# Сума для видачі решти
amount = 113

# Вимірюємо час виконання для жадібного алгоритму
start_time = time.time()
result_greedy = find_coins_greedy(amount)
end_time = time.time()
print("Жадібний алгоритм:", result_greedy)
print("Час виконання жадібного алгоритму:", end_time - start_time)

# Вимірюємо час виконання для алгоритму динамічного програмування
start_time = time.time()
result_dp = find_min_coins(amount)
end_time = time.time()
print("Алгоритм динамічного програмування:", result_dp)
print("Час виконання алгоритму динамічного програмування:", end_time - start_time)
