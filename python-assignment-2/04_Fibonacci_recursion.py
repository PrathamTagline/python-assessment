def fib(n, memo):
    try:
        if memo[n]:
            return memo[n]
    except IndexError:
        pass

    if n == 1 or n == 2:
        result = 1
        memo.insert(0, 0)
        memo.insert(1, result)
        memo.insert(2, result)
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
        memo.insert(n, result)

    return result

print(fib(30, []))