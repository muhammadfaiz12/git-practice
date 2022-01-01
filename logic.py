from database import get_database_rows

def get_neccesary_info(inptcde):
    #made with love by badru
    qr_s = get_database_rows()["result"]
    flag = False
    for z in qr_s:
        if z[0] == inptcde:
            flag = True
            return z[1] 
    
    if (flag == False):
        print("unrecognized city")
        return 1#ya busstop

def calculate_total_bus_stop(codes: list):
    total = 0
    for code in codes:
        total = total + get_neccesary_info(code)
    return total

def calculate_total_possible_route(code):
    pass

