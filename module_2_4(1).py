numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for num in numbers:
    if num > 1:  # Число 1 не является простым и составным
        is_prime = True
        for i in range(2, num - 1): # Не проверяем делением на 1 и само на себя
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

        if not is_prime:
            not_primes.append(num)

print("Primes:", primes)
print("Not Primes:", not_primes)