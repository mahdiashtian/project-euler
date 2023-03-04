def main():
    x = 0
    y = 1
    z = []
    while x <= 4000000:
        x, y = y, y + x
        z.append(x) if x % 2 == 0 else ...
    return z


if __name__ == "__main__":
    print(sum(main()))
