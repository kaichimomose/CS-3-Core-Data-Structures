#!python


def read_route_costs(path):
    routes_cost_dict = {}
    for line in open(path, "r"):
        # route_cost = line.split(',')
        # route, cost = route_cost[0], route_cost[1]
        # route, cost = tuple(route_cost)
        route, cost = line.split(',')  # may not work because it's a list
        routes_cost_dict[route] = cost.strip()  # replace("\n", "")
    return routes_cost_dict


def find_call_cost(routes_cost_dict, phone_number):
    actual_cost = "0"
    for prefix_length in range(1, len(phone_number)+1):
        # slice the phone number to get a candidate prefix for a route
        route = phone_number[0:prefix_length]
        if route in routes_cost_dict:
            actual_cost = routes_cost_dict[route]
    return actual_cost


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        routes_cost_dict = read_route_costs("data/route-costs-106000.txt")
        phone_number = args[0]
        cost = find_call_cost(routes_cost_dict, phone_number)
        output = phone_number + ',' + cost
        print(output)


if __name__ == '__main__':
    main()
