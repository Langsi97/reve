"""
author : [ Langsi ambe Revelation ]
studentnumber : [ 2262920 ]
"""
from re import findall


def dna_match(s: str) -> bool:
    """This function prints true if every substring of the form AATTTA in s,
    that is followed by at most 10 arbitrary nucleotides and
    then followed by the substring GGCTA"""
    # regular expression patern to search DNA sequence

    sequence = r"AATTTA.{0,10}GGCTA"

    #  create a variable result to store the output of the matches.

    result = findall(sequence, s)
    """introducing the condition to chect if matching  
    DNA sequence is present or not in s"""

    if len(result) > 0:  # check if we have atleast one sequence match.
        return True
    return False


print("-------------------------------------------")


def collect_email_from_text(content: str) -> None:
    """the function takes the message and matches all valid emails"""

    patern_1 = r"(^[^.-])(\w+)?([.+?]*)(\w+)(([-.+]*)([a-z0-9])?)*@([^.-])(\w+)([.-])(\w.+)(?<![\.-])"
    emails = list[findall(patern_1, content)]  # selecting valid emails from the content

    # Create a file to write down the valid emails in it
    with open(text, "w") as email_list:
        if len(emails) > 0:
            email_list.write(f"the number of valid emails is {len(emails)}\n")
            # to write the matched emails in the the created file
            for email in emails:
                email_list.write(f"{emails}\n")
        else:
            email_list.write(f"the number of valid emails is{0}")
