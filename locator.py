"""
Building locator, first the name and then passing attributes in a list  so by and value
"""

from collections import namedtuple


Locator = namedtuple('locator', ['by', 'value'])
# Locator_xpath = namedtuple('locator', ['by'])