"""
Text-based parser for ProteinNet Records.
"""

__author__ = "Mohammed AlQuraishi"
__copyright__ = "Copyright 2019, Harvard Medical School"
__license__ = "MIT"

#!/usr/bin/python

# imports
import sys
import re

# Constants
NUM_DIMENSIONS = 3

# Functions for conversion from Mathematica protein files to TFRecords
_aa_dict = {'A': '0', 'C': '1', 'D': '2', 'E': '3', 'F': '4', 'G': '5', 'H': '6', 'I': '7', 'K': '8', 'L': '9', 'M': '10', 'N': '11', 'P': '12', 'Q': '13', 'R': '14', 'S': '15', 'T': '16', 'V': '17', 'W': '18', 'Y': '19'}
_dssp_dict = {'L': '0', 'H': '1', 'B': '2', 'E': '3', 'G': '4', 'I': '5', 'T': '6', 'S': '7'}
_mask_dict = {'-': '0', '+': '1'}

class switch(object):
    """Switch statement for Python, based on recipe from Python Cookbook."""

    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5
            self.fall = True
            return True
        else:
            return False

def letter_to_num(string, dict_):
    """ Convert string of letters to list of ints """
    patt = re.compile('[' + ''.join(dict_.keys()) + ']')
    num_string = patt.sub(lambda m: dict_[m.group(0)] + ' ', string)
    num = [int(i) for i in num_string.split()]
    return num

def read_record(file_, num_evo_entries):
    """ Read a Mathematica protein record from file and convert into dict. """
    
    dict_ = {}

    while True:
        next_line = file_.readline()
        for case in switch(next_line):
            if case('[ID]' + '\n'):
                id_ = file_.readline()[:-1]
                dict_.update({'id': id_})
            elif case('[PRIMARY]' + '\n'):
                primary = letter_to_num(file_.readline()[:-1], _aa_dict)
                dict_.update({'primary': primary})
            elif case('[EVOLUTIONARY]' + '\n'):
                evolutionary = []
                for residue in range(num_evo_entries): evolutionary.append([float(step) for step in file_.readline().split()])
                dict_.update({'evolutionary': evolutionary})
            elif case('[SECONDARY]' + '\n'):
                secondary = letter_to_num(file_.readline()[:-1], _dssp_dict)
                dict_.update({'secondary': secondary})
            elif case('[TERTIARY]' + '\n'):
                tertiary = []
                for axis in range(NUM_DIMENSIONS): tertiary.append([float(coord) for coord in file_.readline().split()])
                dict_.update({'tertiary': tertiary})
            elif case('[MASK]' + '\n'):
                mask = letter_to_num(file_.readline()[:-1], _mask_dict)
                dict_.update({'mask': mask})
            elif case('\n'):
                return dict_
            elif case(''):
                return None

# main. accepts two command-line arguments: input file and the number of entries in evo profiles, and outputs dicts to stdout
if __name__ == '__main__':
    input_path      = sys.argv[1] 
    num_evo_entries = int(sys.argv[2]) if len(sys.argv) == 3 else 20 # default number of evo entries

    input_file = open(input_path, 'r')
        
    while True:
        dict_ = read_record(input_file, num_evo_entries)
        if dict_ is not None:
            print dict_
        else:
            input_file.close()
            break
