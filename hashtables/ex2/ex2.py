
 
# reconstruct_trip(tickets)
# '''
# Understand

# a list of tickets
# put back in order

# ticket has a source
# ticket has a destination
# ticket has an idx

# tickets.idx=0.destination==tickets.idx==1.source

# tickets[idx].destination==tickets[idx+1].source

# tickets out of order

# the are connected one by one

# each desitination is the next tickets source

# loop through the tickets


# '''

# '''

# 10 cities

# 5-6 tickets


# each ticket 2 cities

# list of all cities

# all cities have a source value
# all cites have a desitnation value

# there is a direct order of tickets

# ticket1 [destination]
# ticket2 [source]


# whats the keys

# whats the values

# sources

# destinations

# idx


# idx=0

# 0[source]=1[destination]

# i[source]=(i+1)[destination]


# ## Hints

# * The crux of this problem requires us to 'link' tickets together to
#   reconstruct the entire trip. For example, if we have a ticket `('SJC',
#   'BOS')` that has us flying from San Jose to Boston, then there exists
#   another ticket where Boston is the starting location, `('BOS',
#   'JFK')`. 

# * We can hash each ticket such that the starting location is the key and
#   the destination is the value. Then, when constructing the entire
#   route, the `i`th location in the route can be found by checking the
#   hash table for the `i-1`th location.




# tickets = [
#     Ticket{ source: "PIT", destination: "ORD" },
#     Ticket{ source: "XNA", destination: "CID" },
#     Ticket{ source: "SFO", destination: "BHM" },
#     Ticket{ source: "FLG", destination: "XNA" },
#     Ticket{ source: "NONE", destination: "LAX" },
#     Ticket{ source: "LAX", destination: "SFO" },
#     Ticket{ source: "CID", destination: "SLC" },
#     Ticket{ source: "ORD", destination: "NONE" },
#     Ticket{ source: "SLC", destination: "PIT" },
#     Ticket{ source: "BHM", destination: "FLG" }
# ]
# '''


#     #
#     # Plan
#     # 
#     # I now have all the sources in the table
#     # I can call the first source of none to start it
#     # set a runnervalue or pointer to keep crrnt airport
#     # currnt[source]
#     # 

#     # takeoff=0
#     #flight_plan_order=[]
#     #
#     # takeoff = flight_cache["None"]
#     # for flight in flights:
#     #   flight_plan_order[flight]=cache[takeoff]
#     #   takeoff=cache[takeoff]
#     #   if takeoff is None:
#     #       flight_plan_order.append[takeoff]   
#     #       return 
#     #       
#     #       
#     #       
#     # i have the sources all in the hash lookup
#     # i have an array to add them to one at a time as I find them
#     # i use the value of each loookup as the key for the next one
#     # then i lookup that value as a key to get the next and repeat  
#     #
#     #
#     # 
#     # 
#     # #


# first plan
# 
# Create Ticket Nodes from string pairs
# load Ticket Nodes into a dict
# on each load into the cache, check that each Node isnt a duplicate
# if not a duplicate do both
# 1 add into the dict
# 2 also add to the end of an array at specific point of the dict
# this will allow you to return all values in the order they were addded with no duplicates in constant time   


# second plan
# 
# each Node has a S(start) and an F(finish)
# the F of one Node is the S of one and only one other Node
# we could add a pointer to each of the Nodes on entry
# on hashcache Node creation create an assignment_pointer for the F of the Node finish - Node.f
# on hashcache Node creation create an assignment_pointer for the S of the next Node - Node.Next
# Node.Next = hashcahe[Node.f]
# check for hashcache[finish] 
#
#
# best plan so far

#  we've created a list of the tickets in random order
#  we've looped through the list and added them to the dict in the random order
## we should while loop through the list finding the Node with 'None' as the start value
#  this will be the first addition to the cache and the first addition to hashcache[total_transit] {total_transit:[]}
#  continue while looping through the array Node.
#
# First Draft of Plan 3
#
#  next_flight=null
#  total_transit=[] here or in the if loop?
#  for flight in flights:
#       if flight.source == None:
#           hashcache[flight.source] = flight.destination
#           hashcache['total_transit']=[]
#           hashcache['total_transit'].append(flight.destination)
#           nextflight = flight.destination
#           return or yield?
#  while flight.destination != None:
#       hashcache[flight.source] = flight.destination
#       hashcache['total_transit'].append(flight.destination)
#       nextflight = flight.destination
#  if flight.destination == None:
#       hashcache[flight.source]=flight.destination
#       hashcache['total_transit'].append(flight.destination)            
#       return hashcache['total_transit]            
#                       
#  this will be the first addition to the cache and the first addition to hashcache[total_transit] {total_transit:[]}
#  continue while looping through the array Node.


def reconstruct_trip(flights, LoadFactor):
    hashcache={}
    hashcache['total_transit']=[]
    next_flight=None
    for flight in flights:
        # setting the sources as the key and the destinations as values
        hashcache[flight.source] = flight.destination
    # ⬇⬇this sets next_flight⬇⬇ not to "None" but to the value at key of "None" 
    next_flight=hashcache["NONE"]
    while next_flight != "NONE":
        hashcache['total_transit'].append(next_flight)
        next_flight=hashcache[next_flight]
    if next_flight == "NONE":
        hashcache['total_transit'].append(next_flight)
        return hashcache['total_transit']
        
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    def __str__(self):
        return self.source,self.destination

tickets = [
    Ticket("PIT", "ORD" ),
    Ticket("XNA", "CID" ),
    Ticket("SFO", "BHM" ),
    Ticket("FLG", "XNA" ),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO" ),
    Ticket("CID", "SLC" ),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT" ),
    Ticket("BHM", "FLG" )
]

reconstruct_trip(tickets,None)
