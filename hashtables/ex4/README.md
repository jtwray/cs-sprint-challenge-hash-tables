# Positive and Negative

For an input list of integers, we wish to know which positive numbers
have corresponding negative numbers in the list.

Example input:

```python
[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
```

Input can be in any order.

Example return value:

```python
[ 1, 3, 4 ]
```

Because 1, 3, and 4 are the positive numbers that have corresponding
negative numbers in the list.

Return value can be in any order.

Solve this problem with a hash table.

Limits:

* The input list can contain approximately 5,000,000 elements.

## Plan
## store the real value from zero and store a p or an n
## for each num in num_list load the (num/1).str() into the hashcache['value']=['neg','pos'] || ['null','pos'] || ['neg','null']
#  
# hashing/loadhash function
#    for num in num_list:
#         numster = (num/1).str()
#         hashcache[numster]=[null,null]
#         if num is < 0:
#              hashcache[numster]=[neg,null]
#         else:
#              hashcache[numster]=[null,pos]
#            
# on each load check if the hashcache['value'] already exists
# if it does
#   num is positive?
#       hashcache[num]=[null,null]?
#           hashcache[num]=[pos,null]    
#       hashcache[num]=[null,pos]?
#           hashcache[num]=[null,pos]    
#       hashcache[num]=[neg,null]?
#           hashcache[num]=[neg,pos]    
#            
#   num is negative?
#       hashcache[num]=[null,null]?
#           hashcache[num]=[neg,null]?
#       hashcache[num]=[neg,null]?
#           hashcache[num]=[neg,null]?
#       hashcache[num]=[null,pos]?
#           hashcache[num]=[neg,pos]?
#
#
#
##load completed pairs
# second for loop  
#     hashcache['complete-pairs']=[]
#     for num in nums_list:
#         if hashcache[num] is [neg,pos]:
#             hashcache['completed_pairs].append(num)
# 
# 
# 


## lookup function
# 
def get-completed-pairs:
#          hashcache['completed_pairs']       
#
#
