#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):  # Check if index is out of range
        return s  # If index is invalid, return the original string

    result = ""  # Initialize an empty string to store the modified string
    for i in range(len(s)):
        if i != n:  # Skip the character at index n
            result += s[i]  # Append characters to the result string

    return result
