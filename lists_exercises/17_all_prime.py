def all_prime(nums) -> bool:
    for num in nums:
        if num == 1:
            return False
        for x in range(2, num):
            if num % x == 0:
                return False
    return True


print(all_prime([0, 3, 4, 7, 9]))
print(all_prime([3, 5, 7, 13]))
print(all_prime([1, 5, 3]))
