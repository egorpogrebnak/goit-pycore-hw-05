def caching_fibonacci():
    cache = {}
    def fibonacci(n: int):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            #Якщо число у кеші - повертаємо його
            return cache[n]
        else:
            #Якщо число не знайдено - обраховуємо його рекурсивно
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
