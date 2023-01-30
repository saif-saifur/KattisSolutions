def main():
    N, M = map(int, input().split())
    outcomes = [0] * (N + M + 1)
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            outcomes[i + j] += 1
    max_outcome = max(outcomes)
    for i, outcome in enumerate(outcomes):
        if outcome == max_outcome:
            print(i)

if __name__ == "__main__":
    main()
