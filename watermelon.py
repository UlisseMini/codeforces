w = int(input())
# can w be written as w = 2*a + 2*b for natural a,b? w must be div by 2, and
# w/2 = a + b >= 2 means w >= 4
if w % 2 == 0 and w > 2:
    print('YES')
else:
    print('NO')
