#!/usr/bin/python3
"""
===========================
class MyList
===========================
"""


class MyList(list):
    """MyList that inherits from list"""
    pass

    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))
