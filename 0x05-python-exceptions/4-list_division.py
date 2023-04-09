#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            num_1 = my_list_1[i] if i < len(my_list_1) else 0
            num_2 = my_list_2[i] if i < len(my_list_2) else 0
            division = num_1 / num_2
            if isinstance(division, (int, float)):
                result_list.append(division)
            else:
                print("wrong type")
                result_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except IndexError:
            print("out of range")
            break
        finally:
            pass
    return result_list
