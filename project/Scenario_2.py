#!python

from binarytree import BinarySearchTree
import time


def read_route_costs(path):
    # routes_cost_dict = {}
    binary_search_tree = BinarySearchTree()
    for line in open(path, 'r'):
        route, cost = line.split(',')
        # routes_cost_dict[route] = cost.strip()
        pair = (route, cost)
        binary_search_tree.insert(pair)
    return binary_search_tree


def create_phone_number_lists(path):
    phone_numbers = []
    with open(path, 'r') as f:
        phone_numbers = f.read().splitlines()
    return phone_numbers


def find_call_cost(tree, phone_numbers):
    for phone_number in phone_numbers:
        actual_cost = "0"
        phone_number = phone_number.strip()
        for prefix_length in range(1, len(phone_number)+1):
            # slice the phone number to get a candidate prefix for a route
            route = phone_number[0:prefix_length]
            cost = tree._find_node_iterative(route)
            if cost != "0":
                actual_cost = cost
        if actual_cost == "0":
            actual_cost += "\n"
        write_txt(phone_number, actual_cost)


def write_txt(phone_number, cost):
    with open("route-costs-1000.txt", 'a') as f:
        f.write(phone_number + ',' + cost)


def main():
    start = time.time()
    path = 'data/route-costs-106000.txt'
    tree = read_route_costs(path)
    path_2 = 'data/phone-numbers-1000.txt'
    phone_numbers = create_phone_number_lists(path_2)
    find_call_cost(tree, phone_numbers)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
