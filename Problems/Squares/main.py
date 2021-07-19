n = int(input())


def squares():
    i = 1
    while True:
        yield print(i ** 2)
        i += 1


my_gen = squares()
for x in range(n):
    (next(my_gen))
