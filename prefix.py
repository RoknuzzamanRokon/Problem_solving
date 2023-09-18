# array = [1, 2, 3, 4, 5]
# y = 0

# # for x in array:
# #     y = x + y

# # ns = [x for x in range(1, array) ]


# def prefix(array, sum, list):
#     array
#     pass
    
    
# def prefix_function(result):
    
    
    
    
 
# def fillPrefixSum(arr, n, prefixSum):
  
#     prefixSum[0] = arr[0]
  
#     for i in range(1, n):
#         prefixSum[i] = prefixSum[i - 1] + arr[i]

# if __name__ == '__main__':
#   arr = [10, 4, 16, 20]
#   n = len(arr)

#   prefixSum = []
#   for i in range(n):
#       prefixSum.append(0)
  

#   fillPrefixSum(arr, n, prefixSum)
  
#   for i in range(n):
#       print(prefixSum[i], " ", end="")


given_array = [1,2,3,4,5]
result_array = []

y = 0
for i in given_array:
    y = i + y
    result_array.append(y)


print(result_array)