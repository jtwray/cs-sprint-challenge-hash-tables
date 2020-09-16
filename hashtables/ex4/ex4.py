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




def has_negatives(a):
    num_list = a
    hashcache={}
    nonduplicates=[]
    hashcache['completed_pairs']=[]
 
    for num in num_list:
        if num<0:
            numster = str(-num)
        else:
            numster= str(num)

        if numster in hashcache:
            if num>=0:
                if  hashcache[numster] == [None,'pos']:
                    hashcache[numster] = [None,'pos']    
                if  hashcache[numster] == ['neg',None]:
                    hashcache[numster] = ['neg','pos']    
                if  hashcache[numster] == [None,None]:
                    hashcache[numster] = [None,'pos']    
            if num<0:
                if  hashcache[numster] == ['neg',None]:
                    hashcache[numster] = ['neg',None]
                if  hashcache[numster] == [None,'pos']:
                    hashcache[numster] = ['neg','pos']
                if  hashcache[numster] == [None,None]:
                    hashcache[numster] = ['neg',None]
        else:    
            if num>=0:
                hashcache[numster]=[None,'pos']
            if num<0:
                hashcache[numster]=['neg',None]
        ##load completed pairs
    for num in num_list:
        if num>=0:
            numster=str(num)
        else:
            numster=str(-num)  
        if hashcache[numster] == ['neg','pos']:
            if numster not in hashcache['completed_pairs']:
                hashcache['completed_pairs'].append(numster)
    result = hashcache['completed_pairs']


    return result


print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
# if __name__ == "__main__":
