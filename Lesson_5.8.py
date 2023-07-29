# Напишіть генератор, який видає послідовність простих чисел.

def prime_generator():
    nums = range(2, 100)
    for gen_num in nums:
        for num in range(2, gen_num):
            if gen_num % num == 0:
                break
        else:
            yield gen_num


prime_gen = prime_generator()
for i in range(10):
    print(next(prime_gen))
