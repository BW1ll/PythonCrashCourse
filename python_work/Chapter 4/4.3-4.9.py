for i in range(1, 21):
    print(i)

nums = [value for value in range(1,1_000_000)]
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))

odd_nums = list(range(1, 21, 2))
for num in odd_nums:
    print(num)

multiple3 =  list(range(3, 31, 3))
for num in multiple3:
    print(num)

cubes1 = list(range(1, 11))
for value in cubes1:
    print(value**3)
    

cubes = [value**3 for value in range(1, 11)]
print(cubes)

