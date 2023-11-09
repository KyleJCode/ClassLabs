accounts = [[6,59,64,19,30,76,71,86,90,25,56,17,19,72,61,56,24,40,35,39,67,28,52,11,82,72,8,82,81,47]]
highestWealth = 0
placeholder = 0
for i in range(len(accounts)):
    highestWealth = max(highestWealth, placeholder)
    placeholder = 0
    for j in range(len(accounts[i])):
        placeholder += accounts[i][j]
        if len(accounts) == 1:
            if placeholder > highestWealth:
                highestWealth = placeholder
print(highestWealth)
