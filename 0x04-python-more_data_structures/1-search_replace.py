#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modified_my_list = []
    for idx in range(len(my_list)):
        if my_list[idx] == search:
            modified_my_list.append(replace)
        else:
            modified_my_list.append(my_list[idx])
    return modified_my_list
