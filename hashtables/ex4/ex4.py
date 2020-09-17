## Plan
## store the real value from zero and store a p or an n
## for each num in num_list load the (num/1).str() into the hashcache['value']=['neg','pos'] || ['None','pos'] || ['neg','None']
#  
# hashing/loadhash function
#    for num in num_list:
#         numster = (num/1).str()
#         hashcache[numster]=[None,None]
#         if num is < 0:
#              hashcache[numster]=[neg,None]
#         else:
#              hashcache[numster]=[None,pos]
#            
# on each load check if the hashcache['value'] already exists
# if it does
#   num is positive?
#       hashcache[num]=[None,None]?
#           hashcache[num]=[pos,None]    
#       hashcache[num]=[None,pos]?
#           hashcache[num]=[None,pos]    
#       hashcache[num]=[neg,None]?
#           hashcache[num]=[neg,pos]    
#            
#   num is negative?
#       hashcache[num]=[None,None]?
#           hashcache[num]=[neg,None]?
#       hashcache[num]=[neg,None]?
#           hashcache[num]=[neg,None]?
#       hashcache[num]=[None,pos]?
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
# def get-completed-pairs:
#          hashcache['completed_pairs']       
#
#

######2nd
##### 
#### 
# def has_negatives(arr):
#     hashcache={}
#     hashcache['duplicates']=[]
#     duplicates=[]

#     for num in arr:
#         hashcache[num]=num
#     for num in hashcache:
#         polar_num= (num+(-2*num))
#         if polar_num in hashcache:
#             duplicates.append(num)
            
#         # if num > 0:
#         #     neg_num= (num-(2*num))
#         #     neg_num= (num+(-2*num))
#         # if num <0:
#         #     pos_num= (num+(-2*num))
#         # if num >0 and num - (2*num) in hashcache:
#         #     hashcache['duplicates'].append(abs(num))
#     # return hashcache['duplicates']    
#     return duplicates
####
#####
######
numberstocheck=[1,2,3,4,5,6,7,8,9,0,0,0,1,2,3,1,2,3,-1,-2,-3,-1,-2,-3,-1,-2,-3,1-2,-3]
nums2check=[5,-5,5,1,-1,0,0,2,-2,0,0,2,-2,3,3,3,-3,-3,-3,1,2,3,-4,-4,-4,4,4,4,-4,4,-4]

######3rd
#####
####
def has_negatives(arr):
    hashcache={}
    duplicates=[]
    for num in arr:
        abs_num=abs(num)
        if abs_num in hashcache:
            hashcache[abs_num].append(num)
        else:
            hashcache[abs_num]=[num]
    for num  in hashcache:
      if num !=0 :
        num_pos = hashcache[num].count(num)    
        num_neg = hashcache[num].count(-num)
        if num_neg > 0 and num_pos > 0:
            if num_neg >= num_pos:
                total_pairs=num_pos
            else:
                total_pairs = num_neg
            for time in range(total_pairs):
                duplicates.append(num) 
    return sorted(duplicates,reverse=True)
####
#####
######
#  

print(has_negatives(nums2check))
print(has_negatives(numberstocheck))
# loop through numlist
#   abs_num = abs(num)
#   if num in dict
#       dict[abs_num].append(num)
#   if num not in dict
#       dict[abs_num]=[num]
#   after loading the hashdict
#       access each value of the hashdict and count the instances of +'s and -'s  
#   if num+ > num- totalPairs= num-
#   if num+ < num- totalPairs= num+
#   for time in range(totalpairs):
#       add num to dict['pairs']
  

######1st  
##### 
####
# def has_negatives(a):
#     num_list = a
#     hashcache={}
#     nonduplicates=[]
#     hashcache['completed_pairs']=[]
 
#     for num in num_list:
#         if num<0:
#             numster = str(-num)
#         else:
#             numster= str(num)

#         if numster in hashcache:
#             if num>=0:
#                 # if  hashcache[numster] == [None,'pos']:
#                 #     hashcache[numster] = [None,'pos']    
#                 if  hashcache[numster] == ['neg',None]:
#                     hashcache[numster] = ['neg','pos']    
#                     hashcache['completed_pairs'].append(num)
#                 if  hashcache[numster] == [None,None]:
#                     hashcache[numster] = [None,'pos']    
#             if num<0:
#                 # if  hashcache[numster] == ['neg',None]:
#                 #     hashcache[numster] = ['neg',None]
#                 if  hashcache[numster] == [None,'pos']:
#                     hashcache[numster] = ['neg','pos']
#                     hashcache['completed_pairs'].append(-num)
#                 if  hashcache[numster] == [None,None]:
#                     hashcache[numster] = ['neg',None]
#         else:    
#             if num>=0:
#                 hashcache[numster]=[None,'pos']
#             if num<0:
#                 hashcache[numster]=['neg',None]
#     result = hashcache['completed_pairs']


#     return result
####      
#####      
######      
        ##load completed pairs
    # for num in num_list:
    #     if num>=0:
    #         numster=str(num)
    #     else:
    #         numster=str(-num)  
    #     if hashcache[numster] == ['neg','pos']:
    #         if numster not in hashcache['completed_pairs']:
    #             if num >0:
    #                 hashcache['completed_pairs'].append(num)
    # result = hashcache['completed_pairs']


    # return result


print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
# if __name__ == "__main__":
