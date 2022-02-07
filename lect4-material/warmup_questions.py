def two_sum(nums, target):
    """find two numbers in a list that add up to target"""
    my_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in my_dict:
            return [dict[target - nums[i]], i]
        else:
            my_dict[nums[i]] = i
    return None

def largest(nums):
    """find the largest number"""
    max_num = 0
    for i in nums:
        max_num = max(largest, i)
    return max_num

def nonRepeating(word):
    """find the first non repeating character"""
    chars = {}
    for i in word:
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] += 1

    for k, v in chars.items():
        if v == 1:
            return k

def valid_paren(sentence):
    par = []
    for i in sentence:
        if i == '(':
            par.append(i)
            print(par)
        if i == ')':
            if not par or par[-1] != '(':
                return False
            else:
                par.pop()
    print(par)
    if not par:
        return True
    else:
        return False

#print(twoSum([2,7,11,15], 9))
#print(nonRepeating("abacd"))
#print(validParen("())(abc)))"))