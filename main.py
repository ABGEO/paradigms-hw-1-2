def remove_duplicates(data):
    """
    Remove duplicates from given list.
    List may contain mixed data types.
    :param data: List for removing duplicates from.
    :return: List without duplicate entries.
    """
    already_used_items = {}
    return_data = []

    for item in data:
        # Yes, I know that I can find used items in the return_data,
        # but HW requires this logic.
        if not already_used_items.get(item):
            return_data.append(item)
            already_used_items[item] = True

    return return_data


if __name__ == '__main__':
    data = ['a', 'b', 'c', 'd', 'a', 'e', 'b', 'k', 1, 2, 3, 1, "Squalid", "Poised", "Society", "Poised"]
    data_without_duplicates = remove_duplicates(data)
    print("Initial list:")
    print(data)
    print("List without duplicates:")
    print(data_without_duplicates)
