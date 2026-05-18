def main():
    x = int(input("Was ist x? "))
    print("x zum Quadrat ist", square(x))


def square(n):
    return n + n

if __name__ == "__main__":
    main()