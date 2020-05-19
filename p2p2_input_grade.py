# -*- coding: utf-8 -*-
"""
   Author:  Adam Blanchette
    Email:  tablanch@ncsu.edu
 Unity ID:  tablanch
    Class:  CSC111
 Semester:  Spring 2020
      Lab:

  Program: P2P2 Input Grading Script
 Due Date:

  Purpose: Grading Code
   "Bugs":

#== WORKLOG ==================================================================
  Date   | Time |  Computer name  |  Location  |   Notes
03/21/20 | 1615 | Personal Laptop |    Home    | Completed grading script
         |      |                 |            |
#=============================================================================

#== ACKNOWLEDGEMENTS ==========================================================
Modeled after Dr. Wright's Spring 2019 input grading script
#=============================================================================

"""

#=============================================================================
# IMPORT STATEMENTS
#=============================================================================
import sys                     # to access stdin & stdout
from io import StringIO # for redirecting stdin and stdout
import colorama; colorama.init(autoreset = True)
from colorama import Fore, Style

class colored():
    """ Changes color of text string in terminal. """
    def red        (self, string): return Style.BRIGHT + Fore.RED     + f'{string}'
    def green      (self, string): return Style.BRIGHT + Fore.GREEN   + f'{string}'
    def yellow     (self, string): return Style.BRIGHT + Fore.YELLOW  + f'{string}'
    def blue       (self, string): return Style.BRIGHT + Fore.BLUE    + f'{string}'
    def purple     (self, string): return Style.BRIGHT + Fore.MAGENTA + f'{string}'
    def cyan       (self, string): return Style.BRIGHT + Fore.CYAN    + f'{string}'
    def white      (self, string): return Style.BRIGHT + Fore.WHITE   + f'{string}'
c = colored()

import csc111_input as inp     # module to be graded
#=============================================================================
# MODULE-LEVEL VARIABLES
# module_level_variable2 = 98765
# """int: var  Module level variable documented inline."""
#=============================================================================
PROMPT = 'Enter an integer: '

INT_CASES = [{'id':1, 'prompt':PROMPT, 'upper': 8, 'lower': 2, 'input': 4,              'expect': 4,           'err':'',    'pts':0.5},
             {'id':2, 'prompt':PROMPT, 'upper': 0, 'lower':-10,'input':-7,              'expect':-7,           'err':'',    'pts':0.5},
             {'id':3, 'prompt':PROMPT, 'upper': 3, 'lower':-3, 'input':-3,              'expect':-3,           'err':'',    'pts':0.5},
             {'id':4, 'prompt':PROMPT, 'upper':-3, 'lower':-6, 'input':-3,              'expect':-3,           'err':'',    'pts':0.5},
             {'id':5, 'prompt':PROMPT, 'upper': 8, 'lower': 2, 'input':'15.73',         'expect':'ValueError', 'err':'err', 'pts':0.5},
             {'id':6, 'prompt':PROMPT, 'upper': 8, 'lower': 2, 'input':'9a',            'expect':'ValueError', 'err':'err', 'pts':0.5},
             {'id':7, 'prompt':PROMPT, 'upper': 8, 'lower': 2, 'input':'xyz',           'expect':'ValueError', 'err':'err', 'pts':0.5},
             {'id':8, 'prompt':PROMPT, 'upper': 8, 'lower': 2, 'input':(9, 4),          'expect':4,            'err':'rep', 'pts':0.5},
             {'id':9, 'prompt':PROMPT, 'upper': 3, 'lower':-3, 'input':(9, 0),          'expect':0,            'err':'rep', 'pts':0.5},
             {'id':10,'prompt':PROMPT, 'upper': 10,'lower': 1, 'input':(-4, 25, -3, 7), 'expect':7,            'err':'rep', 'pts':0.5}]

INTS_CASES = [{'id':1, 'num': 5, 'prompt':PROMPT, 'upper': 100, 'lower': 5, 'input': (20, 25, 50, 35, 15),   'expect': [20, 25, 50, 35, 15], 'err':'',    'pts':0.5},
              {'id':2, 'num': 3, 'prompt':PROMPT, 'upper': 8,   'lower': 2, 'input': (4, 3, 7),              'expect': [4, 3, 7],            'err':'',    'pts':0.5},
              {'id':3, 'num': 4, 'prompt':PROMPT, 'upper': 25,  'lower': 0, 'input': (4, 10, 24, 13),        'expect': [4, 10, 24, 13],      'err':'',    'pts':0.5},
              {'id':4, 'num': 1, 'prompt':PROMPT, 'upper': 50,  'lower': 10,'input': (25,),                  'expect': [25],                 'err':'',    'pts':0.5},
              {'id':5, 'num': 5, 'prompt':PROMPT, 'upper': 100, 'lower': 5, 'input': (20, 25,'5.2', 35, 15), 'expect': 'ValueError',         'err':'err', 'pts':0.5},
              {'id':6, 'num': 5, 'prompt':PROMPT, 'upper': 100, 'lower': 5, 'input': (20, '9a', 50, 35, 15), 'expect': 'ValueError',         'err':'err', 'pts':0.5},
              {'id':7, 'num': 4, 'prompt':PROMPT, 'upper': 15,  'lower': 5, 'input': (20, 10, 5, 7, 8),      'expect': [10, 5, 7, 8],        'err':'',    'pts':0.5},
              {'id':8, 'num': 4, 'prompt':PROMPT, 'upper': 15,  'lower': 5, 'input': (10, 20, 5, 0, 7, 8),   'expect': [10, 5, 7, 8],        'err':'',    'pts':0.5},
              {'id':9, 'num': 3, 'prompt':PROMPT, 'upper': 25,  'lower': 10,'input': (20, 25, 50, 35, 15),   'expect': [20, 25, 15],         'err':'',    'pts':0.5},
              {'id':10,'num': 3, 'prompt':PROMPT, 'upper': 25,  'lower': 10,'input': (5, 7, 13, 20, 22),     'expect': [13, 20, 22],         'err':'',    'pts':0.5}]

TEST_NAME = c.cyan('\nTesting ') + c.purple('{0}()') + c.cyan(' case ') + c.purple('{1:d}')
""" format string for a test name """

TEST_RES = c.cyan('Test ') + c.purple('{0} ') + c.cyan('case') + c.purple(' {1:d}') + ' {2}'
""" format string for a test result """

F_STR = c.red("[-0.5] Test {0} failed\nExpected: ") + c.yellow("{1}") + c.red("\nActual: ") + c.yellow("{2}")
F_STR2 = c.red('\nERROR:  p2p2_input module does not contain the ') + c.yellow('{0}') + c.red(' function.\n')

deduct = {'ints':[], 'int': []}
#=============================================================================
# FUNCTIONS/METHODS
# def func(param1, param2):
#     """This function does something with the parameters.
#     Args:
#         param1 (int): The first parameter.
#         param2 (str): The second parameter.
#     Returns:
#         bool:  The return value. True for success, False otherwise.
#         If function does not return a computed value, indicate 
#         "no return value" or "None"
#    """
#    function body statements
#=============================================================================
def in_test(expect, actual):
    """ Type safe testing of actual against expected test values
    Args:
        expect   the expected value
        actual   the actual result from the test
    Returns:
        bool:  True if the arguments are the same type and equal, False otherwise
    """
    if int == type(expect):
        return int == type(actual) and expect == actual
    elif list == type(expect):
        return list == type(actual) and expect == actual
    else:
        return False
    
def test_noerr(inp_func, case):
    """ Executes a test case on an input function that should not generate
        an error
    Args:
        inp_func (function):  the function to test
        case (dict):          the test case data
    Returns:
        bool:   True if the test passed, False otherwise
    """
    
    print(TEST_NAME.format(inp_func.__name__, case['id']))
    # redirect stdout & stdin before testing to capture printed output
    temp_out = sys.stdout
    temp_in = sys.stdin
    sys.stdout = StringIO()
    sys.stdin = StringIO(str(case['input']) + '\n')
    
    # call the function within a try-except in case it throw an unexpected error
    res = False
    try:
        if inp_func.__name__ == 'get_int':
            actual = inp_func(case['prompt'], case['lower'], case['upper'])
            res = in_test(case['expect'], actual)
        elif inp_func.__name__ == 'get_ints':
            inps = ''
            for i in case['input']:
                inps += str(i) + '\n'
            sys.stdin = StringIO(inps)
            actual = inp_func(case['num'], case['prompt'], case['lower'], case['upper'])
            res = in_test(case['expect'], actual)
    except Exception as e:
        actual = repr(e)
        sys.stderr.write(actual)
        res = False
        
    sys.stdout = temp_out
    sys.stdin = temp_in
    print(TEST_RES.format(inp_func.__name__, case['id'], c.green('passed') if res else c.red('failed')))
    if not res: case['actual'] = actual    
    return res
    
def test_err(inp_func, case):
    """ Executes a test case on an input function that should generate
        an error
    Args:
        inp_func (function):  the function to test
        case (dict):          the test case data
    Returns:
        bool:   True if the test passed, False otherwise
    """
    print(TEST_NAME.format(inp_func.__name__, case['id']))
    # redirect stdout & stdin before testing to capture printed output
    temp_out = sys.stdout
    temp_in = sys.stdin
    sys.stdout = StringIO()
    if inp_func.__name__ == 'get_int':
        sys.stdin = StringIO(str(case['input']) + '\n')
    # call the function within a try-except in case it throw an unexpected error
    res = False
    try:
        if inp_func.__name__ == 'get_int':
            actual = inp_func(case['prompt'], case['lower'], case['upper'])
        elif inp_func.__name__ == 'get_ints':
            inps = ''
            for i in case['input']:
                inps += str(i) + '\n'
            sys.stdin = StringIO(inps)
            actual = inp_func(case['num'], case['prompt'], case['lower'], case['upper'])
        sys.stderr.write('{0}() did not raise an error with input {1}\n'.format(inp_func.__name__, case['input']))
    except:
        res = True
    sys.stdout = temp_out
    sys.stdin = temp_in
    print(TEST_RES.format(inp_func.__name__, case['id'], c.green('passed') if res else c.red('failed')))
    if not res: case['actual'] = actual    
    return res
     
def test_reprompt(inp_func, case):
    print(TEST_NAME.format(inp_func.__name__, case['id']))
    # redirect stdout & stdin before testing to capture printed output
    temp_out = sys.stdout
    temp_in = sys.stdin
    sys.stdout = StringIO()
    #sys.stdin = StringIO(case['input'] + '\n')
    # call the function within a try-except in case it throws an unexpected error
    res = False
    try:
        inps = ''
        for i in case['input']:
            inps += str(i) + '\n'
        sys.stdin = StringIO(inps)
        actual = inp_func(case['prompt'], case['lower'], case['upper'])
        res = in_test(case['expect'], actual)
        
    except Exception as e:
        actual = '{0}() raised an unexpected {1} with input {2}\n'.format(inp_func.__name__, repr(e), case['input'])
        sys.stderr.write(actual)
        res = False
    sys.stdout = temp_out
    sys.stdin = temp_in
    print(TEST_RES.format(inp_func.__name__, case['id'], c.green('passed') if res else c.red('failed')))
    if not res: case['actual'] = actual
    return res

def test_get_int():
    """ Executes the tests for the get_int function.
    Returns:  The total score for get_int testing
    """
    score = 0.0
    if not hasattr(inp, 'get_ints'):
        print(F_STR2.format('get_ints'))
        return score
    
    for case in INT_CASES:
        if case['err'] == 'err':
            res = test_err(inp.get_int, case)
        elif case['err'] == 'rep':
            res = test_reprompt(inp.get_int, case)
        else:
            res = test_noerr(inp.get_int, case)
        if res:
            score += case['pts']
        else:
            deduct['int'].append(F_STR.format(case['id'], case['expect'], case['actual']))
            score += 0.0
    return score

def test_get_ints():
    '''Executes tests for the get_ints function.
    Returns: The total score for get_ints testing
    '''
    score = 0.0
    if not hasattr(inp, 'get_ints'):
        print(F_STR2.format('get_ints'))
        return score
    
    for case in INTS_CASES:
        if case['err'] == 'err':
            res = test_err(inp.get_ints, case)
        else:
            res = test_noerr(inp.get_ints, case)
        if res:
            score += case['pts']
        else:
            deduct['ints'].append(F_STR.format(case['id'], case['expect'], case['actual']))
            score += 0.0
            
    return score



#=============================================================================
# MAIN FUNCTION & TESTING AREA
#
# Optional test functions:
# def test_xxx(...)
#     """xxx is the name of the function you are testing
#        document any arguments and return values as normal functions
#     """
#=============================================================================

def main():
    """Description of main() - what does this function do?  Does it run a 
    program?  Does it execute test code?"""
    
    int_score = test_get_int()
    print('-'*40)
    ints_score = test_get_ints()
    
    print(c.cyan("\nFinal score for " + c.purple('get_int()') + c.cyan('  is ') + c.purple(f'{int_score:.2f}')))
    if deduct['int'] != []:
        for deduction in deduct['int']:
            print(deduction)
            print('')
        
    print(c.cyan("Final score for " + c.purple('get_ints()') + c.cyan(' is ') + c.purple(f'{ints_score:.2f}')))
    if deduct['ints'] != []:
        for deduction in deduct['ints']:
            print(deduction)
            print('')
        
    print(c.cyan('\nThe total score earned for ') + c.purple('csc111_input') + c.cyan(' is ') + c.purple('{:.2f}').format(sum((int_score, ints_score))))



if __name__ == '__main__':
    main()
