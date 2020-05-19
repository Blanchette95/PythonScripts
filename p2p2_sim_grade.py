# -*- coding: utf-8 -*-
"""
   Author:  Adam Blanchette
    Email:  tablanch@ncsu.edu
 Unity ID:  tablanch
    Class:  CSC111, Spring 2020
      Lab:  N/A

  Program:  Project 2 Part 2 Grading Script
 Due Date:  

  Purpose:  Grading code

   "Bugs":  [A list of remaining problems/omissions, or "None"]

#== WORKLOG ==================================================================
  Date   | Time |    Computer name    |  Location  |   Notes
03/21/20 | 2030 |   Personal Laptop   |    Home    | Added test functions for print_welcome,
         |      |                     |            | print_goodbye, and main functions.
         |      |                     |            | Updated and improved test functions for 
         |      |                     |            | calc_boarded and run_sim
03/22/20 | 2030 |   Personal Laptop   |    Home    | Finished run_sim test function and 
         |      |                     |            | the deduction output 
03/23/20 | 1800 |   Personal Laptop   |    Home    | Implemented the test_main function and
         |      |                     |            | tweaked other tests to ensure they worked
         |      |                     |            | correctly. Other bug fixes and error
         |      |                     |            | handling added.
03/28/20 | 1400 |   Personal Laptop   |    Home    | Bug fixes and updated tests
#=============================================================================

#== AKNOWLEDGEMENTS ==========================================================
Took inspiration from Jake Raynor's improvements to the run_sim test function for Fall 2019 
#=============================================================================

"""

#=============================================================================
# IMPORT STATEMENTS
#=============================================================================
import p2p2_sim as sim
import string
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

class prints():
    '''Created by Jake Raynor
    Allows the output to be read from the run_sim function
    Updated to work with Python 3'''
    def __init__(self): pass
    def __enter__(self):
        import sys
        from io import StringIO
        self.temp_out = sys.stdout
        sys.stdout = self.test_out = StringIO()

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        global rprint
        sys.stdout = self.temp_out
        self.test_out.seek(0)
        rprint = self.test_out.readlines()
        try:
            rprint = [x[:x.index('\n')] for x in rprint]
        except:
            rprint = [x for x in rprint]


P_STR = c.cyan('calc_boarded test ' ) + c.purple('{0:>2d}') + c.green(' passed')
F_STR1 = c.cyan('calc_boarded test ' ) + c.purple('{0:>2d}') + c.red(' failed')
F_STR2 = c.cyan('\nExpected: ') + c.yellow('{1:<2d}') + c.cyan(' Actual: ') + c.yellow('{2:<2}')
F_STR =  F_STR1 + F_STR2

F_STR3 = c.red('p2p2_sim module does not contain the ') + c.yellow('{0}') + c.red(' function.\n')
F_STR4 = c.red('calc_boarded test') + c.yellow(' {0:>2d} ') + c.red('failed \nExpected: ') + c.yellow('{1:<2d}') + c.red(' Actual: ') + c.yellow('{2:<2}')

HEAD = '''
---------------------------------------------
Iterations Current   Boarding Departing
---------------------------------------------'''
SIM_TEST = c.cyan("\nTest Case: ") + c.purple("{0}") + c.cyan("\nIterations  = ") + c.purple("{1}") + c.cyan("\nBoard Rates = ") + c.purple("{2}") + c.cyan("\nExit Rates  = ") + c.purple("{3}")
SIM_LINE = '{0:^10d}{1:^10d}{2:^10d}{3:^10d}'

pts = {'print_welcome': 0.0, 'print_goodbye': 0.0, 'calc_boarded': 0.0, 'run_sim': 0.0, 'main': 0.0, 'ui': 0.0, 'format': 0.0}
deduct = {'print_welcome': [], 'print_goodbye': [], 'calc_boarded': [], 'run_sim': [], 'main': [], 'ui': [], 'format': []}
#=============================================================================
# FUNCTIONS/METHODS
#=============================================================================
def get_spaces(data):
    '''Created by Jake Raynor
    Gets the spaces from the student's output to be used later'''
    spaces = []
    for row in data:
        for i in range(len(row)):
            if row[i] in '-'+string.digits:
                y = list(row)
                y[i] = 'X'
                row = ''.join(y)
        spaces.append([x for x in row.split('X') if x != ''])
    return spaces

def table_data(data, example):
    new_data = [[x for x in row.split(' ') if x != ''] for row in data]
    
    tab_data = []
    for i1 in range(len(new_data)):
        
        row = new_data[i1]
        val = example[i1]
        
        for i2 in range(len(row)):
            num = row[i2]
            x = val[i2]
            if num == str(x):
                row[i2] = get_spaces(data)[i1][i2] + c.green(num)
            else:
                row[i2] = get_spaces(data)[i1][i2] + c.red(num)
        tab_data.append(''.join(row))
    
    return tab_data

def print_run_sim(stops, boarding, exiting, example):
    '''Outline by Jake Raynor
    This was updated by Adam Blanchette to fit the Spring 2020 project.
    Removed redundancies and updated to streamline the process
    Parameters:
        stops (int): Number of stops the bus makes
        boarding (list): List of boarding rates
        exiting (list): List of exit rates
        example (list): Example to be referenced against
    '''
    global rprint
    with prints(): sim.run_sim(stops, boarding, exiting)
    data = [x for x in rprint if x != '']
    table  = []
    count  = 0
    for row in data:
        if row.strip()[0] in string.digits: count += 1
    try: # Checking if student included a header in run_sim
        header = []
#        labels = []
        data = data[:count]
        footer = rprint[count+3:]
        tab_data = table_data(data, example)
    except IndexError:
        try:
            header = []
#            labels = rprint[0]
            data   = rprint[1:]
            footer = rprint[count+4:]
        
            tab_data = table_data(data, example)
        except IndexError:
            header = rprint[:3]
#            labels = rprint[1]
            data   = rprint[3:]
            footer = rprint[count+4:]
            if footer != '':
                del data[-1]
            tab_data = table_data(data, example)
    footer = [c.green(x) for x in footer]
    
    table += header + tab_data + footer
    for row in table: print(row)


def test_print_welcome():
    global rprint
    print(c.purple("\nTESTING PRINT_WELCOME()\n"))
    if not hasattr(sim, 'print_welcome'):
        print(F_STR3.format('print_welcome'))
        deduct['print_welcome'].append(c.red('[-5] ') + F_STR3.format('print_welcome'))
        return
    name = sim.print_welcome.__name__
    print(c.cyan('An appropriate and neatly formatted welcome message should be '))
    print(c.cyan('output to the console following this message\n'))
    try:
        with prints(): sim.print_welcome()
        for line in rprint:
            print(c.green(line))
        if 'n' not in input('\nGood welcome message? (y/n) ').lower():
            pts[name] += 5.0
        elif sim.print_welcome() != None:
            pts[name] += 2.5
            deduct[name].append(c.red('[-2.5] Function returns instead of prints'))
        else:
            deduct[name].append(c.red('[-5] print_welcome() failed'))
    except Exception:
        deduct[name].append(c.red('[-5] print_welcome() failed'))

def test_print_goodbye():
    global rprint
    print(c.purple("\nTESTING PRINT_GOODBYE()\n"))
    if not hasattr(sim, 'print_goodbye'):
        print(F_STR3.format('print_goodbye'))
        deduct['print_goodbye'].append(c.red('[-5] ') + F_STR3.format('print_goodbye'))
        return
    name = sim.print_goodbye.__name__
    print(c.cyan('An appropriate and neatly formatted exit message should be '))
    print(c.cyan('output to the console following this message\n'))
    try:
        with prints(): sim.print_goodbye()
        for line in rprint:
            print(c.green(line))
        if 'n' not in input('\nGood exit message? (y/n) ').lower():
            pts[name] += 5.0
        elif sim.print_goodbye() != None:
            pts[name] += 2.5
            deduct[name].append(c.red('[-2.5] Function returns instead of prints'))
        else:
            deduct[name].append(c.red('[-5] print_goodbye failed'))
    except Exception:
        deduct[name].append(c.red('[-5] print_goodbye failed'))

def test_calc_boarded():
    print(c.purple('\nTESTING CALC_BOARDED()\n'))
    if not hasattr(sim, 'calc_boarded'):
        print(F_STR3.format('calc_boarded'))
        deduct['calc_boarded'].append(c.red('[-5] ') + F_STR3.format('calc_boarded'))
        return
    name = sim.calc_boarded.__name__
    cases = [{'case':1,  'boarding': 20, 'departing': 10, 'current': 15, 'expected': 25, 'pts': 0.5},
             {'case':2,  'boarding': 20, 'departing': 10, 'current':  5, 'expected': 20, 'pts': 0.5},
             {'case':3,  'boarding':  5, 'departing': 10, 'current': 15, 'expected': 10, 'pts': 0.5},
             {'case':4,  'boarding':  3, 'departing':  0, 'current':  0, 'expected':  3, 'pts': 0.5},
             {'case':5,  'boarding': 10, 'departing': 12, 'current': 12, 'expected': 10, 'pts': 0.5},
             {'case':6,  'boarding': 18, 'departing': 15, 'current': 12, 'expected': 18, 'pts': 0.5},
             {'case':7,  'boarding': 18, 'departing': 14, 'current': 16, 'expected': 20, 'pts': 0.5},
             {'case':8,  'boarding': 11, 'departing': 18, 'current': 17, 'expected': 11, 'pts': 0.5},
             {'case':9,  'boarding': 14, 'departing': 10, 'current': 20, 'expected': 24, 'pts': 0.5},
             {'case':10, 'boarding': 15, 'departing': 18, 'current': 15, 'expected': 15, 'pts': 0.5}]
    
    for case in cases:
        try:
            actual = sim.calc_boarded(case['boarding'], case['departing'], case['current'])
        except Exception as e:
            actual = repr(e)
        if actual == case['expected']:
            print(P_STR.format(case['case']))
            pts[name] += case['pts']
        else:
            print(F_STR.format(case['case'], case['expected'], str(actual)))
            deduct[name].append(c.red('[-1] ') + F_STR4.format(case['case'], case['expected'], str(actual)))

def test_run_sim():
    score = 20.0
    print(c.cyan('\nTESTING RUN_SIM()\n'))
    if not hasattr(sim, 'run_sim'):
        print(F_STR3.format('run_sim'))
        deduct['run_sim'].append(c.red('[-20] ') + F_STR3.format('run_sim'))
        return
    name = sim.run_sim.__name__
#    Test 1
    ds = c.yellow('Test 1:')
    stops = 10
    boarding = [10, 20, 10]
    exiting = [30, 25, 15]
    out1 = [[1,  0, 10,  0],
            [2, 10, 20, 10],
            [3, 20, 10, 15],
            [4, 15, 10, 15],
            [5, 10, 20, 10],
            [6, 20, 10, 15],
            [7, 15, 10, 15],
            [8, 10, 20, 10],
            [9, 20, 10, 15],
            [10,15, 10, 15]]
    try:
        print(SIM_TEST.format(1, stops, boarding, exiting))
        print(c.cyan("Expected:" + HEAD))
        for stop, curr, board, depart in out1:
            print(c.cyan(SIM_LINE.format(stop, curr, board, depart)))
        print(c.cyan("\nActual output (4 points):"))
        print_run_sim(stops, boarding, exiting, out1)
        check = input("\nDoes actual match expected? (y/n) ")
        if 'n' in check.lower():
            if 'y' in input('Is there any output? (y/n)'):
                stop_check = input("Is last stop calculated correctly? (y/n) ")
                exit_check = input("Is exiting column different? (y/n) ")
                if 'n' in stop_check.lower():
                    score -= 1
                    ds += c.red('\n[-1] Final stop calculated incorrectly')
                if 'y' in exit_check.lower():
                    score -= 0.5
                    ds += c.red('\n[-0.5] Exiting column calculated incorrectly')
                if 'y' not in stop_check and 'n' not in exit_check:
                    score -= 4.0
                    ds += c.red('\n[-4] Test 1 failed')
            else:
                score -= 4.0
                ds += c.red('\n[-4] Test 1 failed')
        else:
            score -= 0.0
    except ValueError:
        score -= 20.0
        print(c.red("run_sim prompts for user input. Grader needs to go into student's code to fix it."))
        deduct[name].append(c.red("[-10] run_sim prompts for user input. Grader needs to go into student's code to fix it."))
        return
    except Exception as e:
        score -= 4.0
        print(c.red("Test 1 raised ") + c.yellow(repr(e)))
        ds += c.red("\n[-4] Test 1 raised ") + c.yellow(repr(e))
    finally:
        if ds != c.yellow('Test 1:'):
            deduct[name].append(ds)

#    Test 2
    ds = c.yellow('Test 2:')
    stops = 15
    boarding = [7, 15, 10, 5, 10]
    exiting = [19, 5, 14, 11, 10]
    out2 = [[ 1,  0,  7,  0],
            [ 2,  7, 15,  5],
            [ 3, 17, 10, 14],
            [ 4, 13,  5, 11],
            [ 5,  7, 10,  7],
            [ 6, 10,  7, 10],
            [ 7,  7, 15,  5],
            [ 8, 17, 10, 14],
            [ 9, 13,  5, 11],
            [10,  7, 10,  7],
            [11, 10,  7, 10],
            [12,  7, 15,  5],
            [13, 17, 10, 14],
            [14, 13,  5, 11],
            [15,  7, 10,  7]]

    try:
        print(SIM_TEST.format(2, stops, boarding, exiting))
        print(c.cyan("Expected:" + HEAD))
        for stop, curr, board, depart in out2:
            print(c.cyan(SIM_LINE.format(stop, curr, board, depart)))
        print(c.cyan("\nActual output (4 points):"))
        print_run_sim(stops, boarding, exiting, out2)
        check = input("\nDoes actual match expected? (y/n) ")
        if 'n' in check.lower():
            if 'y' in input('Is there any output? (y/n)'):
                stop_check = input("Is last stop calculated correctly? (y/n) ")
                exit_check = input("Is exiting column different? (y/n) ")
                if 'n' in stop_check.lower():
                    score -= 1
                    ds += c.red('\n[-1] Final stop calculated incorrectly')
                if 'y' in exit_check.lower():
                    score -= 0.5
                    ds += c.red('\n[-0.5] Exiting column calculated incorrectly')
                if 'n' not in stop_check and 'y' not in exit_check:
                    score -= 4.0
                    ds += c.red('\n[-4] Test 2 failed')
            else:
                score -= 4.0
                ds += c.red('\n[-4] Test 2 failed')
        else:
            score -= 0.0
    except Exception as e:
        score -= 4.0
        print(c.red("Test 2 raised ") + c.yellow(repr(e)))
        ds += c.red("\n[-4] Test 2 raised ") + c.yellow(repr(e))
    finally:
        if ds != c.yellow('Test 2:'):
            deduct[name].append(ds)

#    Test 3
    ds = c.yellow('Test 3:')
    stops = 20
    boarding = [10, 13, 7, 14, 12, 14, 19, 8]
    exiting = [18, 4, 18, 4, 18, 4, 18, 4]
    out3 = [[ 1,  0, 10,  0],
            [ 2, 10, 13,  4],
            [ 3, 19,  7, 18],
            [ 4,  8, 14,  4],
            [ 5, 18, 12, 18],
            [ 6, 12, 14,  4],
            [ 7, 22, 19, 18],
            [ 8, 23,  8,  4],
            [ 9, 27, 10, 18],
            [10, 19, 13,  4],
            [11, 28,  7, 18],
            [12, 17, 14,  4],
            [13, 27, 12, 18],
            [14, 21, 14,  4],
            [15, 31, 19, 18],
            [16, 32,  8,  4],
            [17, 36, 10, 18],
            [18, 28, 13,  4],
            [19, 37,  7, 18],
            [20, 26, 14,  4]]

    try:
        print(SIM_TEST.format(3, stops, boarding, exiting))
        print(c.cyan("Expected:" + HEAD))
        for stop, curr, board, depart in out3:
            print(c.cyan(SIM_LINE.format(stop, curr, board, depart)))
        print(c.cyan("\nActual output (4 points):"))
        print_run_sim(stops, boarding, exiting, out3)
        check = input("\nDoes actual match expected? (y/n) ")
        if 'n' in check.lower():
            if 'y' in input('Is there any output? (y/n)'):
                stop_check = input("Is last stop calculated correctly? (y/n) ")
                exit_check = input("Is exiting column different? (y/n) ")
                if 'n' in stop_check.lower():
                    score -= 1
                    ds += c.red('\n[-1] Final stop calculated incorrectly')
                if 'y' in exit_check.lower():
                    score -= 0.5
                    ds += c.red('\n[-0.5] Exiting column calculated incorrectly')
                if 'n' not in stop_check and 'y' not in exit_check:
                    score -= 4.0
                    ds += c.red('\n[-4] Test 3 failed')
            else: 
                score -= 4.0
                ds += c.red('\n[-4] Test 3 failed')
        else:
            score -= 0.0
    except Exception as e:
        score -= 4.0
        print(c.red("Test 3 raised ") + c.yellow(repr(e)))
        ds += c.red("\n[-4] Test 3 raised ") + c.yellow(repr(e))
    finally:
        if ds != c.yellow('Test 3:'):
            deduct[name].append(ds)

#    Test 4
    ds = c.yellow('Test 4:')
    stops = 8
    boarding = [14, 12, 7, 14]
    exiting = [14, 6, 5, 8]
    out4 = [[1,  0, 14,  0],
            [2, 14, 12,  6],
            [3, 20,  7,  5],
            [4, 22, 14,  8],
            [5, 28, 14, 14],
            [6, 28, 12,  6],
            [7, 34,  7,  5],
            [8, 36, 14,  8]]

    try:
        print(SIM_TEST.format(4, stops, boarding, exiting))
        print(c.cyan("Expected:" + HEAD))
        for stop, curr, board, depart in out4:
            print(c.cyan(SIM_LINE.format(stop, curr, board, depart)))
        print(c.cyan("\nActual output (4 points):"))
        print_run_sim(stops, boarding, exiting, out4)
        check = input("\nDoes actual match expected? (y/n) ")
        if 'n' in check.lower():
            if 'y' in input('Is there any output? (y/n)'):
                stop_check = input("Is last stop calculated correctly? (y/n) ")
                exit_check = input("Is exiting column different? (y/n) ")
                if 'n' in stop_check.lower():
                    score -= 1
                    ds += c.red('\n[-1] Final stop calculated incorrectly')
                if 'y' in exit_check.lower():
                    score -= 0.5
                    ds += c.red('\n[-0.5] Exiting column calculated incorrectly')
                if 'n' not in stop_check and 'y' not in exit_check:
                    score -= 4.0
                    ds += c.red('\n[-4] Test 4 failed')
            else: 
                score -= 4.0
                ds += c.red('\n[-4] Test 4 failed')
        else:
            score -= 0.0
    except Exception as e:
        score -= 4.0
        print(c.red("Test 4 raised ") + c.yellow(repr(e)))
        ds += c.red("\n[-4] Test 4 raised ") + c.yellow(repr(e))
    finally:
        if ds != c.yellow('Test 4:'):
            deduct[name].append(ds)

#    Test 5
    ds = c.yellow('Test 5:')
    stops = 10
    boarding = [15, 5, 9, 10, 15, 10]
    exiting = [12, 15, 7, 15, 7, 9]
    out5 = [[ 1,  0, 15,  0],
            [ 2, 15,  5, 15],
            [ 3,  5,  9,  5],
            [ 4,  9, 10,  9],
            [ 5, 10, 15,  7],
            [ 6, 18, 10,  9],
            [ 7, 19, 15, 12],
            [ 8, 22,  5, 15],
            [ 9, 12,  9,  7],
            [10, 14, 10, 14]]

    try:
        print(SIM_TEST.format(5, stops, boarding, exiting))
        print(c.cyan("Expected:" + HEAD))
        for stop, curr, board, depart in out5:
            print(c.cyan(SIM_LINE.format(stop, curr, board, depart)))
        print(c.cyan("\nActual output (4 points):"))
        print_run_sim(stops, boarding, exiting, out5)
        check = input("\nDoes actual match expected? (y/n) ")
        if 'n' in check.lower():
            if 'y' in input('Is there any output? (y/n)'):
                stop_check = input("Is last stop calculated correctly? (y/n) ")
                exit_check = input("Is exiting column different? (y/n) ")
                if 'n' in stop_check.lower():
                    score -= 1
                    ds += c.red('\n[-1] Final stop calculated incorrectly')
                if 'y' in exit_check.lower():
                    score -= 0.5
                    ds += c.red('\n[-0.5] Exiting column calculated incorrectly')
                if 'n' not in stop_check and 'y' not in exit_check:
                    score -= 4.0
                    ds += c.red('\n[-4] Test 5 failed')
            else: 
                score -= 4.0
                ds += c.red('\n[-4] Test 5 failed')
        else:
            score -= 0.0
    except Exception as e:
        score -= 4.0
        print(c.red("Test 5 raised ") + c.yellow(repr(e)))
        ds += c.red("\n[-4] Test 5 raised ") + c.yellow(repr(e))
    finally:
        if ds != c.yellow('Test 5:'):
            deduct[name].append(ds)

    pts[name] = score

def test_main():
    print(c.purple("\nTESTING MAIN()\n"))
    if not hasattr(sim, 'main'):
        print(F_STR3.format('main'))
        deduct['main'].append(c.red('[-10] ') + F_STR3.format('main'))
        return
    name = sim.main.__name__
    du = '' # Deduction string for user input
    dm = '' # Deduction string for main function
    df = '' # Deduction string for formatted output
    out_str = c.cyan('This is a test for the main function. The goal for this function is to\n')
    out_str+= c.cyan('test how the student\'s code functions in the context of the module. This\n')
    out_str+= c.cyan('checks if the code shows a welcome and goodbye message, as well as if the\n')
    out_str+= c.cyan('user is prompted for the correct information. Given the nature of the other\n')
    out_str+= c.cyan('tests, there is only a need to run the main function once. Just enter the\n')
    out_str+= c.cyan('following information when prompted.\n\n')
    out_str+= c.cyan('Number of stops on route: ') + c.purple('3\n\n')
    out_str+= c.cyan('Boarding rate for ')+ c.blue('Stop 1: ') + c.purple('8\n')
    out_str+= c.cyan('Boarding rate for ')+ c.blue('Stop 2: ') + c.purple('10\n')
    out_str+= c.cyan('Boarding rate for ')+ c.blue('Stop 3: ') + c.purple('8\n\n')
    out_str+= c.cyan('Exiting rate for  ')+ c.blue('Stop 1: ') + c.purple('5\n')
    out_str+= c.cyan('Exiting rate for  ')+ c.blue('Stop 2: ') + c.purple('10\n')
    out_str+= c.cyan('Exiting rate for  ')+ c.blue('Stop 3: ') + c.purple('10\n\n')
    out_str+= c.cyan('Number of iterations run: ') + c.purple('10\n\n')
    print(out_str)
    
    try:
        sim.main()    
        if 'n' in input("\nProgram displayed welcome message? (y/n)"):
            dm += c.red('[-1] Did not display welcome message\n')
        else: pts[name] += 1.0
        if 'n' in input('Program displayed goodbye message? (y/n)'):
            dm += c.red('[-1] Did not display goodbye message\n')
        else: pts[name] += 1.0
        
        check_input = input("\nProgram prompted for correct user input? (y/n) ")
        if 'n' in check_input:
            dm += c.red('[-3] Didn\'t prompt for correct user input\n')
            pot = []
            if 'n' in input('Prompted for number of stops? (y/n)'):
                pot.append('n')
                du += c.red('[-1] Didn\'t prompt for number of stops\n')
            if 'n' in input('Prompted for boarding rates? (y/n)'):
                pot.append('n')
                du += c.red('[-1] Didn\'t prompt for boarding rates\n')
            if 'n' in input('Prompted for exiting rates? (y/n)'):
                pot.append('n')
                du += c.red('[-1] Didn\'t prompt for exiting rates\n')
            if 'n' in input('Prompted for number of iterations? (y/n)'):
                pot.append('n')
                du += c.red('[-1] Didn\'t prompt for number of iterations\n')
            if pot == ['n', 'n', 'n', 'n']: #jackpot
                du = c.red('[-5] No user input\n')
        else:
            pts['ui'] = 5.0
            pts['main'] += 3.0
       
        check_run = input("Program ran the simulation? (y/n)")
        if 'n' in check_run:
            dm += c.red('[-5] Program did not run simulation')
            df += c.red('[-5] Program did not run simulation')
        else:
            pts['main'] += 5.0
            if 'n' in input("Program had nicely formatted output? (y/n)"):
                df += c.red('[-5] Incorrect or poor formatting')
            else: pts['format'] += 5.0

    except Exception as e:
        dm += c.red('[-10] Program raised ') + c.yellow(repr(e))
        df += c.red('[-5] Program raised ') + c.yellow(repr(e))
        du += c.red('[-5] Program raised ') + c.yellow(repr(e))
    finally:
        if dm != '': deduct['main'].append(dm)
        if du != '': deduct['ui'].append(du)
        if df != '': deduct['format'].append(df)
    
#=============================================================================
# MAIN METHOD & TESTING AREA
#=============================================================================

def main():
    tests = [test_print_welcome, test_print_goodbye, test_calc_boarded, test_run_sim, test_main]
#    tests = [test_run_sim]
    for test in tests:
        test()

    print('', end = '\n\n')
    for test in tests:
        name = test.__name__[5:]

        string = c.cyan('Final score for ') + c.purple('{0:<13} ') + c.cyan('is ') + c.purple('{1:.2f}')
        print(string.format(name, pts[name]))
        if deduct[name] != []:
            for deduction in deduct[name]:
                print(deduction + '\n')

    print(string.format('user input', pts['ui']))
    if deduct['ui'] != []:
        for deduction in deduct['ui']: print(deduction)
    print(string.format('formatting', pts['format']))
    if deduct['format'] != []:
        for deduction in deduct['format']: print(deduction)

    total = str(sum(pts[k] for k in pts.keys()))
    print(c.cyan('\n\nTotal score for ') + c.blue('p2p2_sim.py') + c.cyan(' is ') + c.purple(total))

if __name__ == '__main__':
    main()
    
 
