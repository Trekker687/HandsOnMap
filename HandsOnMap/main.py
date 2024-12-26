numbers1 = [1,2,3]
numbers2 = [4,5,6]
print("Original lists: ", numbers1, numbers2)

result = list(map(lambda x, y: x+y, numbers1, numbers2))
print("List after addition: ", result)

nums = [1,2,3,4,5,6,7]
def sq(n): 
    return n*n
square = list(map(sq,nums))
print("Original list: ", nums)
print("Square of list: ", square)
