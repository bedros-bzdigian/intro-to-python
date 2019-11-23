def show_list_nums(nums):
     for i in nums:
        yield (i)

l = show_list_nums([1,2,3,4,5])

for i in range(0,5):
        print (next(l))
