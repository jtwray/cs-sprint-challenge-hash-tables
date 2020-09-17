# Intersections of Multiple Lists

Find the intersection between multiple lists of integers.

Do not use numpy or sets to solve this; use `dict` or hashtables,
please.

We're given a list of lists that contain integers:

```python
[
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]
```

And we need to compute the _intersection_, that is, numbers that exist
in all lists.

From the above input, the return value will be:

```
[1, 2]
```

Because those are the numbers that exist in all the lists.

(Output can be in any order.)

Limits:

* There can be up to 10 lists in the list of lists.
* The lists can contain up to roughly 1,000,000 elements each.


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