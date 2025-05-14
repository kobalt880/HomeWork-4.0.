def find_minimal_element(list: list[int]) -> int | None:
    if len(list) > 0 and all([isinstance(e, int) and e > 0 for e in list]):
        min = list[0]

        for e in list:
            if e < min:
                min = e
        return min

def find_average(lst: list[int]) -> float | None:
    if len(lst) > 0 and all([isinstance(e, int) and e > 0 for e in lst]):
        return sum(lst) / len(lst)
    
def find_second_max(lst: list[int]) -> int:
    if len(lst) > 1 and all([isinstance(e, int) and e > 0 for e in lst]):
        new_lst = list(set(lst))
        new_lst.remove(max(new_lst))

        return max(new_lst)
    
def find_sum_among_even(lst: list[int]) -> int:
    if len(lst) > 0 and all([isinstance(e, int) and e > 0 for e in lst]):
        new_list = [e for e in lst if e % 2 == 0]
        return sum(new_list)

def is_monotonous(lst: list[int]) -> int:
    if len(lst) > 0 and all([isinstance(e, int) and e > 0 for e in lst]):
        for i in range(len(lst)-1):
            if lst[i] >= lst[i+1]:
                increasing = False
                break
        else:
            increasing = True
        
        for i in range(len(lst)-1):
            if lst[i] <= lst[i+1]:
                decreasing = False
                break
        else:
            decreasing = True

        return decreasing or increasing
