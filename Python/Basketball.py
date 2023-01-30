def winner(scores):
    alice = 0
    barbara = 0
    for i in range(0, len(scores), 2):
        if scores[i] == 'A':
            alice += int(scores[i+1])
        else:
            barbara += int(scores[i+1])
        if (alice >= 11 or barbara >= 11) and abs(alice - barbara) >= 2:
            break
    if alice > barbara:
        return 'A'
    else:
        return 'B'

scores = input()
print(winner(scores))
