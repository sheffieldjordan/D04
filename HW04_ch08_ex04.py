#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check hether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """This function returns boolean values, meaning it will stop running once either
    True or False is returned. Replacing the boolean values with strings (e.g. 'lower' 
    instead of True and 'upper' instead of False), would result in the function running
    through every character ('c') in the argument string before ending.  
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """The .islower() string method is invoked on the string 'c'. Because the string
    'c' includes only a lower case character, this function will always return True.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """This will return whatever the most-recent boolean value is. Thus, if the last
    letter is upper case, it will always return False, even if the other letters are 
    lower.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """This works as expected. Flag will be set to True and stay that way, once c.islower()
    happens to be True once
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag



def any_lowercase5(s):
    """This is similar to the first function. This function stops running once it 
    reaches an upper case character, returning False.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1("Oakland")) #returns False, but should return True because 'akland' is lower case
    print(any_lowercase2("OAKLAND")) #returns True when it should return False, since no letters are lower case
    print(any_lowercase3("oaklanD")) #will always return False, since the last letter is upper case
  
    print(any_lowercase5("oakLand")) #returns False, despite lower case characters.




if __name__ == '__main__':
    main()
