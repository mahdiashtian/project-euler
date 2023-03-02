def main():
    range_3 = range(0, 1000, 3)
    range_5 = range(0, 1000, 5)
    return sum(list(range_3) + list(set(range_5) - set(range_3)))


if __name__ == "__main__":
    print(main())
