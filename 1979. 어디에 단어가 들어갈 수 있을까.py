num = int(input())
sol = list()

for _ in range(num):
    N, K = map(int, input().split())
    Box = list()
    result = 0
    for i in range(N):
        Box.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if Box[i][j] == 1:
                n = 0
                while Box[i + n][j] == 1:
                    if i + n >= N - 1:
                        break
                    elif Box[i + n + 1][j] == 0:
                        break
                    n += 1
                if n == K - 1:
                    if Box[i - 1][j] != 1:
                        result += 1
                    elif i == 0:
                        result += 1
                m = 0
                while Box[i][j + m] == 1:
                    if j + m >= N - 1:
                        break
                    elif Box[i][j + m + 1] == 0:
                        break
                    m += 1
                if m == K - 1:
                    if Box[i][j - 1] != 1:
                        result += 1
                    elif j == 0:
                        result += 1
    sol.append(result)

for i in range(len(sol)):
    print("#%d %d" % (i + 1, sol[i]))
