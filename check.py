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
    <BLANKLINE>
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


def check_purchase():
    '''
    >>> check_purchase()
    PROPERTY DETAILS
    ================
    square footage: 242
    bedrooms: 2
    bathrooms: 2
    <BLANKLINE>
    HOUSE DETAILS
    # of stories: 3
    garage: attached
    fenced yard: yes
    PURCHASE DETAILS
    selling price: $100,000
    estimated taxes: $4,000
    '''
    purchase = main.HousePurchase()
    purchase.price = "$100,000"
    purchase.taxes = "$4,000"
    purchase.num_bedrooms = "2"
    purchase.num_baths = "2"
    purchase.fenced = "yes"
    purchase.garage = "attached"
    purchase.square_feet = "242"
    purchase.num_stories = "3"
    purchase.display()


def check_agent():
    agent = main.Agent()
    agent.add_property()
    agent.display_properties()


if __name__ == '__main__':
    doctest.testmod()
