#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    modified_list = []

    # Iterate through the elements in the original list
    for item in my_list:
        # Check if the current element is equal to the 'search' element
        if item == search:
            # If it matches, add the 'replace' element to the modified list
            modified_list.append(replace)
        else:
            # If it doesn't match, keep the original element in the modified list
            modified_list.append(item)

    return modified_list
