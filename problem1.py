print('hiisgay')

sum = 0
for i in range(3,1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i, i / 3, i % 3)
        sum = sum + i
        print(sum)

