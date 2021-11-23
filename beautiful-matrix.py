for i in range(5):
    row = input().split(' ')
    for j in range(5):
        if row[j] == '1':
            # shift to coordinates relative to the center of the matrix
            x, y = i-2, j-2
            # manhattan distance to 1
            print(abs(x) + abs(y))
            exit()



