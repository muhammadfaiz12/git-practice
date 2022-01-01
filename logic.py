from database import get_database_rows

# Function to get number of stop in a city
def get_neccesary_info(code):
    data = get_database_rows()["result"]

    for city in data:
        if city[0] == code:
            return city[1] 

    # No city match found
    print("unrecognized city")
    return 1

def calculate_total_bus_stop(codes: list):
    total = 0
    for code in codes:
        total = total + get_neccesary_info(code)
    return total

def calculate_total_possible_route(codes: list):
    total = 1
    for code in codes:
        total = total * get_neccesary_info(code)
    return total

