def is_sorted(lst: list) -> bool:
    """
    function to check if the input array is sorted or not
    one element arrays and empty arrays are sorted.
    """
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True


# print(is_sorted([1, 0]))
