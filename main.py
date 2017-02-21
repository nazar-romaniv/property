def get_valid_input(input_string, valid_options):
    '''
    Checks if the passed input matches one of the printed options and returns the input.
    input_string -- message printed at input
    valid_options -- the valid options expected by the caller

    '''
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    '''
    Base class for House and Apartment.
    '''

    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        '''
        :square_feet: The area of the property.
        :beds: The number of bedrooms.
        :baths: The number of bathrooms.
        :kwargs: Keyword arguments for compatibility with multiple inheritance.
        '''
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        '''
        Prints out the information on the property.
        '''
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    @staticmethod
    def prompt_init():
        '''
        Requests for the input of the characteristics of the property.
        '''
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))


class Apartment(Property):
    '''
    The class for work with apartments.
    '''

    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        '''
        :param balcony: Contains the information about the balcony of the apartment ("yes", "no", "solarium").
        :param laundry: Contains the information about the laundry of the apartment ("coin", "ensuite", "none").
        '''
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        '''
        Displays the information on the apartment.
        '''
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))
        print("has balcony:".format(self.balcony))
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in \
                Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property have? ({})".format(
                            ", ".join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input(
                            "Does the property have a balcony? "
                            "({})".format(
                            ", ".join(Apartment.valid_balconies)))
        parent_init.update({
                            "laundry": laundry,
                            "balcony": balcony
        })
        return parent_init

    @staticmethod
    def prompt_init():
        '''
        Calls the methods prompt_init() of class Property and returns the dictionary
        with the information on the apartment.
        '''
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init


class House(Property):
    '''
    The class for work with houses.
    '''

    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        '''
        :param num_stories: Number of stories in the house.
        :param garage: One of the following: "attached", "detached", "none".
        :param fenced: Tells whether the house is fenced.
        '''
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        '''
        Displays the information on the house.
        '''
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    @staticmethod
    def prompt_init():
        '''
        Requests the information on the house and stores it into a dictionary.
        '''
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
        House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
        House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
             "garage": garage,
            "num_stories": num_stories
        })
        return parent_init


class Purchase:
    '''
    The class to implement the purchase of a property.
    '''

    def __init__(self, price='', taxes='', **kwargs):
        '''
        :price: The price of the property.
        :taxes: The taxes paid.
        '''
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        '''
        Prints out the information on the purchase.
        '''
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    @staticmethod
    def prompt_init():
        '''
        Gets the information on the purchase and outputs it as a dictionary.
        '''
        return dict(
                price=input("What is the selling price? "),
                taxes=input("What are the estimated taxes? "))

class Rental:
    '''
    Implements the rental of a property.
    '''

    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        '''
        :furnished: Either yes or no.
        :utilities: The sum of the utilities.
        :rent: The amount of rent.
        '''
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        '''
        Displays the information on the rented property.
        '''
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
        self.utilities))
        print("furnished: {}".format(self.furnished))

    @staticmethod
    def prompt_init():
        '''
        Stores the information about the rental in a dictionary.
        '''
        return dict(
            rent = input("What is the monthly rent? "),
            utilities = input("What are the estimated utilities? "),
            furnished = get_valid_input(
        "Is the property furnished? ",
        ("yes", "no")))


class HouseRental(Rental, House):
    '''
    Implements the rental of a house.
    '''

    @staticmethod
    def prompt_init():
        '''
        Stores the information on the rental in a dict.
        '''
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentRental(Rental, Apartment):
    '''
        Implements the rental of an apartment.
        '''

    @staticmethod
    def prompt_init():
        '''
        Stores the information on the rental in a dict.
        '''
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentPurchase(Purchase, Apartment):
    '''
    Implements the purchase of an apartment.
    '''

    @staticmethod
    def prompt_init():
        '''
        Stores the information on the purchase in a dict.
        '''
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class HousePurchase(Purchase, House):
    '''
    Implements the purchase of a house.
    '''

    @staticmethod
    def prompt_init():
        '''
        Stores the information on the purchase in a dict.
        '''
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class Agent:
    '''
    Implements the main functionality.
    '''

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        '''
        Prints out the information on all the properties of the agent.
        '''
        for property in self.property_list:
            property.display()


    def add_property(self):
        '''
        Adds a property to the list of properties.
        '''
        property_type = get_valid_input(
         "What type of property? ",
         ("house", "apartment")).lower()
        payment_type = get_valid_input(
         "What payment type? ",
         ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
         (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
