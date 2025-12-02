count = 0
prev3 = int(input())
prev2 = int(input())
prev1 = int(input())
for i in range(0, 1997):
    curr = int(input())
    if(prev1 + prev2 + prev3 < prev1 + prev2 + curr):
        count += 1
    prev3 = prev2
    prev2 = prev1
    prev1 = curr
print("count is " + str(count))