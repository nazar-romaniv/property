def get_valid_input(input_string, valid_options):
    '''
    Checks if the passed input matches one of the printed options and returns the input.
    :input_string: Message printed at input
    :valid_options: The valid options expected by the caller
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
        :balcony: Contains the information about the balcony of the apartment ("yes", "no", "solarium").
        :laundry: Contains the information about the laundry of the apartment ("coin", "ensuite", "none").
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
        :num_stories: Number of stories in the house.
        :garage: One of the following: "attached", "detached", "none".
        :fenced: Tells whether the house is fenced.
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

    @staticmethod
    def multiple_input(message, *options):
        opt = list(options)
        output = {}
        print(message)
        inp = '\n'
        while not inp == '':
            for i in opt:
                print(i)
            inp = input()
            if '=' not in inp or inp.count('=') > 1:
                continue
            index = inp.find('=')
            if inp[:index].strip() not in options:
                continue
            output.update({inp[:index].strip(): inp[index + 1:].strip()})
            try:
                opt.remove(inp[:index].strip())
            except ValueError:
                pass
        return output

    @staticmethod
    def set_of_dict(dictionary):
        a = set()
        for key in dictionary:
            a.add((key, dictionary[key]))
        return a

    def find_property(self):
        kind = get_valid_input('What kind of property do you want to find?', ('apartment', 'house'))
        action = get_valid_input('Purchase or rental?', ('purchase', 'rental'))
        PropertyClass = Agent.type_map[(kind, action)]
        if (kind, action) == ('apartment', 'purchase'):
            attributes = ['balcony', 'laundry', 'beds', 'baths', 'price', 'taxes', 'square_feet']
        elif (kind, action) == ('apartment', 'rental'):
            attributes = ['balcony', 'laundry', 'beds', 'baths', 'furnished', 'utilities', 'rent', 'square_feet']
        elif (kind, action) == ('house', 'purchase'):
            attributes = ['fenced', 'garage', 'beds', 'baths', 'price', 'taxes', 'square_feet']
        else:
            attributes = ['balcony', 'laundry', 'beds', 'baths', 'furnished', 'utilities', 'rent', 'square_feet']
        search_request = Agent.multiple_input('Enter search parameters: ', *attributes)
        for property in self.property_list:
            if Agent.set_of_dict(property.__dict__()).issuperset(Agent.set_of_dict(search_request)):
                return property
        else:
            print('Not found')

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
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
