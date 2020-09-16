
## plan
# create a hashcache 
# for each list
#    loop through items in list
#    create a pointer for string(item)
#    check dict for itempointer
#    if there add 1 to count at  dict[pointeritem][0]
#    if not there add it in and set count to 1    
#    if count is equalt to total arrays length add the item to list hashcache['inall3'][...,...,...]
#


 
# PSEUDO CODE PLAN
# create a dict
# for each list
# for item in items_list:
#    itemster=str(item)
#    if  dict[itemster]:
#        dict[itemster][0]+=1
#    else:
#        dict[itemster]=[1,item]
#
#    if dict[itemster][0]==total_arrs_length:
#        dict['inall3']=[]
#        dict['inall3'].append(itemstr)



myarrs=[
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

def intersection(arrays):
    arrs_total_length=len(arrays)
    hashcache={}
    hashcache['inall3']=[]
    for list in arrays:
        for item in list:
            itemster=str(item)
            if itemster in hashcach
                hashcache[itemster][0]+=1
            else:
                hashcache[itemster]=[1,item]

            if hashcache[itemster][0]==arrs_total_length:
                hashcache['inall3'].append(item)
    result = hashcache['inall3']

    return result

res= intersection(myarrs)

print(myarrs)
print(res)
# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))



