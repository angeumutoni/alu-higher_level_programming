#!/usr/bin/python3
class MyList(list):
    ''' creating a public instance method '''

    def print_sorted(self):
        ''' printing the sorted list '''
        print(sorted(self))
