"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    mappedList = map(str, items)

    items = list(mappedList)

    for i in items:
        x = items.count(i)
        frequencies.update({i : x})
        
    return frequencies
