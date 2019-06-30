import math


def square_of_circle(radius=5, n=100000):
    """Calculates a square of a circle by dividing
     it into {n} smaller rings, calculate theirs
     lengths. The sum of all inner rings' lengths
     is approximately equals to the real square.."""

    pi = math.pi
    print("Original square is: ", pi*radius**2)
    width = radius / n
    all_r = [radius]
    while all_r[-1] - width > 0:
        all_r.append((all_r[-1] - width))
    rectangle_squares = [2*pi*r*width for r in all_r]
    print(sum(rectangle_squares))


if __name__ == '__main__':
    square_of_circle()
