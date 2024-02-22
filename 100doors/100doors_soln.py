
doors = [False] * 101

for i in range(1,101):
    for j in range(i, 101, i):
        doors[j] = not doors[j]

for i in range (1, 101):
    if doors[i] is True:
        print(i, end=", ")


# doors = [False] * 101
# k = 2
# l = 2

# for i in range(1, 101):
#     doors[i] = not doors[i]
#     print(doors)

#     for j,k,l in range(k, 101, l):
#         k+=1
#         l+=1
#         doors[j] = not doors[j]
#         print("j: ", j, doors)
