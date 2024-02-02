def solution(x, y):
    x, y = int(x), int(y)
    cycles = 0

    while x != 1 or y != 1:
        if (
            x < 1 or y < 1 or x == y
        ):  # If x or y is less than 1 or x == y (unless both are 1), they are invalid
            return "impossible"
        elif x > y:
            timesOfMulti = (x - 1) // y  # how many y are in x
            x -= y * timesOfMulti  # getting the x for next cycle
            cycles += timesOfMulti
        else:  # Vice versa
            timesOfMulti = (y - 1) // x
            y -= x * timesOfMulti
            cycles += timesOfMulti

    return str(cycles)


print(solution("1000000000000", "1"))
