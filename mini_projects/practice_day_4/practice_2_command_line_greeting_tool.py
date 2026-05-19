import sys

def main():
    
    if len(sys.argv) < 2:
        sys.exit("Zu wenige Argumente")
    if len(sys.argv) > 2:
        sys.exit("Zu viele Argumente")

    name = sys.argv[1].strip().title()
    print("Hello,", name)


if __name__ == "__main__":
    main()
