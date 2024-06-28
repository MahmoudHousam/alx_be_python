def draw_pattern():
    pos_num = int(input("Enter the size of the pattern: "))
    for _ in range(pos_num):
        for _ in range(pos_num):
            print("*", end="")
        print()


if __name__ == "__main__":
    draw_pattern()
