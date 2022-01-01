from logic import *
print("this is an simple bus app")
while(True):
    user_input = input("please input the city code (<code> <code> <code>)")
    new_items = user_input.split(" ")
    total = calculate_total_bus_stop(new_items)
    possible_route = calculate_total_possible_route(new_items)

    print("There are in total "+str(total)+" bus stops")
    print("There are in total "+str(possible_route)+" possible route")
