from cs50 import get_int

while True:
    h = get_int("Height: ")
    if h > 0 and h < 9:
        break
    print("enter number more than 0 and less than 9")

for i in range(1, h + 1):
    print(" " * (h - i) + "#" * i, end="")
    print()