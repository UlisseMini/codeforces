input()
xs = [int(x) for x in input().split(' ')]


# we for sure need to get every number to -1 or 1. picking whichever is closer
# means we cannot waste moves this way (eg. if we wanted -3 to go to 1 we would
#  have to go through -1 anyway, so this is always safe)
# note that 0 is a special case, we always need to switch 0 -> -1 or 1 (otherwise the
#  product would be zero) so adding 1 for every zero is correct.

moves = 0
has_zeros = False
negatives = 0
for x in xs:
    if x == 0:
        has_zeros = True
        moves += 1
    else:
        negatives += x < 0
        # smallest distance to -1 or 1
        moves += min(abs(x+1), abs(x-1))

if not has_zeros and negatives % 2 == 1:
    # if we have an odd number of -1's then add two moves to fix that
    moves += 2

print(moves)
