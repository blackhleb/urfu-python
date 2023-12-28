def spiralMove(N):
    x, y = 0, 0
    dx, dy = -1, 0
    step = 1

    for i in range(N):
        for j in range(2):
            for k in range(step):
                x += dx
                y += dy
                N -= 1
                if N == 0:
                    return x, y
            dx, dy = -dy, dx
        step += 1
    return x, y


N = int(input())
x, y = spiralMove(N)
print(x, y)
