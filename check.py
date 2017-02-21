'''
Module for checking the functionality of main.py.
'''
import main
import doctest

def check_house():
    '''
    >>> check_house()
    PROPERTY DETAILS
    ================
    square footage: 120
    bedrooms: 3
    bathrooms: 2

    HOUSE DETAILS
    # of stories: 2
    garage: none
    fenced yard: no
    '''
    my_house = main.House()
    my_house.square_feet = 120
    my_house.num_bedrooms = 3
    my_house.num_baths = 2
    my_house.num_stories = 2
    my_house.garage = "none"
    my_house.fenced = "no"
    my_house.display()

if __name__ == '__main__':
    doctest.testmod()