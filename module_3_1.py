import random

calls = 0

def count_calls():
    global calls
    calls += 1
    return

def string_info(string):
    string = (len(string), string.upper(), string.lower())
    count_calls()
    return string

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            return True
    return False
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
