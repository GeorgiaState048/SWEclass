import math
import os

def problem1(word):
    vowels = set(['a','e','i','o','u'])

    numVowels = 0
    numCons = 0
    for i in word: 
        if i in vowels:
            numVowels += 1
        else:
            numCons += 1
    if numVowels > numCons:
        return True
    elif numCons > numVowels:
        return False
    else:
        return None

def problem2(r, h):
    return (math.pi)*h*r*r

def problem3(words):
    return ','.join(words)

def problem4(listWords):
    for i in range(len(listWords)):
        listWords[i] = problem3(listWords[i])
    f = open("hw3", "x")
    for i in listWords:
        f.write(i)
    f.close()
    return os.path.abspath("hw3")

def problem5(file):
    text = open(file, "r")
    lines = text.readlines()
    print(lines)
    final = []
    
    for line in lines:
        final.append(line.split(','))
    
    return final

def problem6(x, y):
    try:
        print(x/y)
    except:
        print("the second number is 0 so the value is undefined")

def problem7(nums):
    nums = set(nums)
    nums = list(nums)
    return nums

def problem8():
    directory = "hw3-folder"
    parent_dir = "C:/Users/jonat/OneDrive/Documents/VisualStudioRepositories/SoftwareEngineering"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)


print(problem1("String"))
#print(problem2(3,4))
#print(problem3(["this", "is", "a", "test"]))
#print(problem4([["this", "is", "a", "test"],["Jonathan", "is", "a", "test"],["Python", "is", "a", "test"]]))
#print(problem5("theFile.txt"))
#print(problem6(6,3))
#print(problem7([1,1,3,5,3,1,2]))
#problem8()