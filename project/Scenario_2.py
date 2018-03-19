#!python

from binarytree import BinarySearchTree

def read_route_costs(path):
    # routes_cost_dict = {}
    binary_search_tree = BinarySearchTree()
    for line in open(path, 'r'):
        route, cost = line.split(',')
        # routes_cost_dict[route] = cost.strip()
        pair = (route, cost)
        binary_search_tree.insert(pair)
    return binary_search_tree

def find_call_cost(tree, path):
    for phone_number in open(path, 'r'):
        phone_number = phone_number.strip()
        cost = tree._find_node_iterative(phone_number)
        if cost == "0":
            cost += "\n"
        write_txt(phone_number, cost)

def write_txt(phone_number, cost):
    with open("route-costs-1000.txt", 'a') as f:
        f.write(phone_number + ',' + cost)

def main():
    path = 'data/route-costs-106000.txt'
    tree = read_route_costs(path)
    path_2 = 'data/phone-numbers-1000.txt'
    find_call_cost(tree, path_2)

if __name__ == '__main__':
    main()
