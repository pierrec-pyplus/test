def my_add(a, b):
    result = a + b
    return result


def test_my_add():
    assert my_add(3, 2) == 5


def main():
    result = my_add(3, 2)
    print(result)
    print("\n\n")


if __name__ == "__main__":
    main()
