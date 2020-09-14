class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
 

flight_cache={}

def LoadingTickets(tickets):
    for ticket in tickets:
        source=ticket[source]
        destination=ticket[destination]
        flight_cache[source]=destination


def reconstruct_flight_plan(flights):
    LoadingTickets(flights)
    takeoff=0
    flight_plan_order=[]
    takeoff = flight_cache["None"]

    for flight in flights:
        flight_plan_order[flight]=flight_cache[takeoff]
        takeoff=flight_cache[takeoff]
        if takeoff is None:
            flight_plan_order.append[takeoff]
            return flight_plan_order

def reconstruct_trip(tickets):
    reconstruct_flight_plan(tickets)

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

 
 
reconstruct_trip(tickets)
'''
Understand

a list of tickets
put back in order

ticket has a source
ticket has a destination
ticket has an idx

tickets.idx=0.destination==tickets.idx==1.source

tickets[idx].destination==tickets[idx+1].source

tickets out of order

the are connected one by one

each desitination is the next tickets source

loop through the tickets


'''

'''

10 cities

5-6 tickets


each ticket 2 cities

list of all cities

all cities have a source value
all cites have a desitnation value

there is a direct order of tickets

ticket1 [destination]
ticket2 [source]


whats the keys

whats the values

sources

destinations

idx


idx=0

0[source]=1[destination]

i[source]=(i+1)[destination]


## Hints

* The crux of this problem requires us to 'link' tickets together to
  reconstruct the entire trip. For example, if we have a ticket `('SJC',
  'BOS')` that has us flying from San Jose to Boston, then there exists
  another ticket where Boston is the starting location, `('BOS',
  'JFK')`. 

* We can hash each ticket such that the starting location is the key and
  the destination is the value. Then, when constructing the entire
  route, the `i`th location in the route can be found by checking the
  hash table for the `i-1`th location.




tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
]
'''


    #
    # Plan
    # 
    # I now have all the sources in the table
    # I can call the first source of none to start it
    # set a runnervalue or pointer to keep crrnt airport
    # currnt[source]
    # 

    # takeoff=0
    #flight_plan_order=[]
    #
    # takeoff = flight_cache["None"]
    # for flight in flights:
    #   flight_plan_order[flight]=cache[takeoff]
    #   takeoff=cache[takeoff]
    #   if takeoff is None:
    #       flight_plan_order.append[takeoff]   
    #       return 
    #       
    #       
    #       
    # i have the sources all in the hash lookup
    # i have an array to add them to one at a time as I find them
    # i use the value of each loookup as the key for the next one
    # then i lookup that value as a key to get the next and repeat  
    #
    #
    # 
    # 
    # #