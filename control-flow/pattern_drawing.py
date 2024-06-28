def draw_pattern():
    pos_num = int(input("Enter the size of the pattern: "))
    case = 0
    while pos_num > case:
        for _ in range(pos_num):
            for _ in range(pos_num):
                print("*", end="")
            print()
            case += 1


if __name__ == "__main__":
    draw_pattern()
