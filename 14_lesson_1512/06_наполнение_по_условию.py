nums = []
i = 1

while len(nums) <= 12 and i <= 1000:
    if i % 17 == 0:
        nums.append(i)
    i += 1

print(nums)



