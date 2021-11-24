nums = [4, 5, 7, 2, 0, 2, 0, 1, 9, 0, 5, 0, 12, 0]

# среднее В1
summary = 0
for num in nums:
    summary += num  # каждое следующее число складываю с суммой предыдущих чисел

# среднее В2
mid = sum(nums) / len(nums)  # сумма / длину

for index in range(len(nums)):  # каждый индекс в списке
    if nums[index] == 0:  # если число с текущим индексом - это 0
        nums[index] = mid  # заменить его на среднее арифметическое
 
print(nums)
