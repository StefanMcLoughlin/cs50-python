from practice_1_calculator import square

def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 zum Quadrat war nicht 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 zum Quadrat war nicht 9")

if __name__ == "__main__":
    main()