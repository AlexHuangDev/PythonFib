# Fibonacci Sequence
# By Alex Huang
# Recursive and Iterative Fibonacci Pattern using Python
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...


def fib_recursive(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n):
    if n <= 1:
        return n

    a = 1
    b = 1

    for i in range(2, n):
        temp = a
        a += b
        b = temp

    return a


def retry_fib():
    choice = str(input("Do you want to try again? (y/n): ")).lower()
    if choice.startswith("y"):
        main()
    else:
        print("Goodbye.")


def main():
    while True:
        try:
            n = int(input("Input the nth term you want from the Fibonacci Sequence: "))
            assert n >= 0
            nth_term_recursive = fib_recursive(n)
            print("Recursive answer:", nth_term_recursive)
            nth_term_iterative = fib_iterative(n)
            print("Iterative answer:", nth_term_iterative)
            retry_fib()
            break
        except:
            print("Enter a positive integer!")

main()
