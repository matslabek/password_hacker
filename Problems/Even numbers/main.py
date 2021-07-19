n = int(input())


def even():
    i = 0
    while True:
        yield i
        i += 2

my_gen = even()
for x in range(n):
    print(next(my_gen))
# Don't forget to print out the first n numbers one by one here