"""Functions to parse a file containing villager data."""

# orders in the file
# name -> species -> personality -> hobby -> motto

import doctest
filename = open("villagers.csv")

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    # species = [1]
    species = set([])

    filename = open("villagers.csv")
    for line in filename:
        line = line.rstrip() #remote white space from the right
        words = line.split('|')

        species.add(words[1])
    # TODO: replace this with your code

    return species

# print(all_species(filename))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
 


    villagers = []

    filename = open("villagers.csv")
    for line in filename:
        # line = line.rstrip() # remote white space from the right
        villager_name, species = line.rstrip().split('|')[:2]

        # name = [0] species = [1] personality = [2]
        if search_string in ("All", species):
            villagers.append(villager_name)
        
    #     #if species matches input of species we will return the villager name associated
    # for words[1] in line:
    #     if words[1] == search_string:
    #         print(words[0])
    #     # if the species matches the search_species
    #         # append that species's owners name to the list 
    #         villagers.append(words[0])
    # else:
    #     # else
    #     # add everyone's name to the list 
    #     villagers.append(words[0])
    return sorted(villagers)

print(get_villagers_by_species(filename, search_string="All"))
# print(get_villagers_by_species(filename, search_string="Wolf"))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    main_list = []
    #make a fitness list of people who have that hobby
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    # list = [hobby[name]] fit{audie, cyrano}
    # list(sorted(hobbies_list(---names inside list become sorted---)))
    
    # 6 hobbies = fitness, Nature, Education, Music, Fashion, Play

    # TODO: replace this with your code
    filename = open("villagers.csv")
    for line in filename:
        line = line.rstrip() 
        words = line.split('|')
        #remote white space from the right
        # villager_name, hobbies = line.rstrip().split('|')[:4]
        villager_name = words[0]
        hobbies = words[3]

        if "fitness" in hobbies:
            fitness.append(villager_name)
        # elif villager has nature for hobby
            # nature.append(villager) 
        print(fitness)

   # our return value should be a list with 6 lists inside 
   # the names in each list should appear in alphabetical order

   # main_list = [[fitness], [nature], [education], [music], [fashion], [play]]
    return []
print(all_names_by_hobby(filename))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
