# To generate kridathon_keys

import datetime
x = datetime.datetime.now()
key_year = (str(x.year)[2:])
key_month = str(x.month)
key_day = str(x.day)

for i in range (1,101):
    event_key = "E"+key_year+key_month+key_day+(str(10000+i))
    print("Event key for event number "+str(i)+ "is :" +event_key)
    for j in range (1,11):
        tournament_key = event_key+"T"+(str(100+j))
        print("Tournament keys for event number "+str(i)+ "is :" +tournament_key)

"""Note that the two for() loops applied above are just to show how key will be actually generated.
The "i" will mean the primary key of event table and "j" will mean the primary key of tournament table.
This function is capable of generating 90,000 unique event key and 90,00,000 tournament key each day"""
