#arbitrary arguements

def add_sums(*nums):
    sum=0
    for num in nums:
        sum+=num
    return sum
    
print("total:", add_sums(2,9,7,11,8))