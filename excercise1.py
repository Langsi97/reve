import re


def count_char(rev):
    digits = len(re.findall(r'\d', rev))   # finding the total number digits

    # looking for the number  of non-digits characters
    non_digits = len(re.findall(r'\D', rev))

    # searching for total  white spaces
    white_spaces = len(re.findall(r'\s', rev))

    words = len(re.findall(r'\w+', rev))  # giving the total number of words

    # returning the expected results

    dictionary = {'digits': digits, 'non-digits': non_digits,
                  'white spaces': white_spaces, "words": words}
    return dictionary


# testing the codes
rev = 'my name is revelation  i am 26 years old'
dictionary = count_char(rev)
print(dictionary)
