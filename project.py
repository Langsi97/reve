"""
 Author: [Ambe Revelation Langsi]
 Studentnumber: [2262920]
"""


import csv
import pandas as pd

"""-----------------------Question 1--------------------------"""


def read_csv(file_path):
    """
    - Firstly,I read the CSV file using a csv reader which
      returns the data as a list of lists.
    - Next, I use pandas to convert this list of list to a dataframe.
    - I added a column name to the data that looks like the one presented 
    in the example of the project.  

    Args:
    file_path (str): The path to the CSV file to read.

    Returns:
    A pandas dataframe.
    """
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        data = [row for row in csvreader]
        df = pd.DataFrame(
            data, columns=['SegmentNr', 'Position', 'A', 'C', 'G', 'T'])
        return df


"""------------------Question 2----------------------"""

# writing python code to clean the data with respect to the specified errors in
# the question paper.


 