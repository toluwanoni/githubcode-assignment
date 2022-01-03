#if_else statements in python
weight_allowed_at_naija_airports = input("weight_allowed_at_naija_airports: " )

weight_allowed_at_ghana_airports = input("weight_allowed_ghana_airports: ")

if weight_allowed_at_naija_airports < weight_allowed_at_ghana_airports:
    print("your luggage will have no delay")
elif weight_allowed_at_naija_airports > weight_allowed_at_ghana_airports:
    print("you will have to pay extrafee for the luggages")
else:
    print("there wont be any problem with the merchandise")