# -*- coding: utf-8 -*-
"""
   Author:  Adam Blanchette
    Email:  tablanch@ncsu.edu
 Unity ID:  tablanch
    Class:  CSC111, Spring 2018
      Lab:  N/A

  Program:  Test Codes

  Purpose:  For miscellaneous test scripts or anything else useful

   "Bugs":  None

#== WORKLOG ==================================================================
           Date          | Time | Computer Name | Location | Notes |
Tue Aug 29 16:24:29 2017 | 2230 |   My Laptop   |          |       |


#=============================================================================

#== ACKNOWLEDGEMENTS ==========================================================
Note any and all help you received on this program module, including class
notes, Piazza, etc.

#=============================================================================

"""
#==============================================================================
# IMPORT STATEMENTS
#==============================================================================
#import turtle
import random
#import time
#import numpy as np



#==============================================================================
#  MODULE-LEVEL VARIABLES
#  module_level_variable2 = 98765
#  """int: Module level variable documented inline."""
#==============================================================================



#==============================================================================
# FUNCTIONS/METHODS
#==============================================================================

def move(trtl, x, y):  # from in-class 10
    trtl.penup()
    trtl.goto(x, y)
    trtl.pendown()

def ext_angle(sidenum):
    angle = 360.0/sidenum
    return angle

def draw_poly_at(trtl, x, y, sides, length, line, fill):
    move(trtl, x, y)
    trtl.color(line, fill)
    trtl.begin_fill()
    turn = ext_angle(sides)
    for i in range(sides):
        trtl.forward(length)
        trtl.left(turn)
    trtl.end_fill()

    
def drunk_walk(trtl, trips):
    for i in range(trips):
        trtl.left(random.randint(-360, 360))
        trtl.forward(random.randint(1, 100))

def M_border():
    arr0 = np.ones([10,10])
    arr0[1:9,1:9] = np.zeros([8,8])
    print arr0

def get_compound_words():
    """This function prompts the user for two file names. The first will be the
    name of a text file containing the English dictionary, and the second file
    will be the name of the output file. The dictionary file should be 
    formatted as a plain text file with a single word on each line and must 
    contain at least one word. The output file, if it exists, will be 
    overwritten by this program.
    Args:
        
    Returns:
        
    """
    num_compound = 0
    valid = True
    while valid:
        valid = False
        try:
            file_name_1 = raw_input("Enter the file name containing the dictionary: ")
            with open(file_name_1, 'rb') as f:
                dictionary = f.read().split()
                file_name_2 = raw_input("Enter the output file name: ")
                with open(file_name_2, 'wb') as out_file:
                    for word in dictionary:
                        for i in range(len(word)):
                            if word[:i] in dictionary and word[i:] in dictionary:
                                num_compound += 1
                                comp_word = (word + ' = ' + word[:i] + ' + ' + word[i:] + '\n')
                                out_file.write(str(comp_word))
                    out_file.write(str(num_compound))     
                
        except IOError:
            print "This file does not exist"
            valid = True

#==============================================================================
# def read(filein, fileout):
#     with open(filein, 'rb') as fin:
#         with open(fileout, 'wb') as fout:
#             header = fin.readline()
#             fout.write(header)
#             reader = csv.reader(fin)
#             writer = csv.writer(fout)
#             for q in reader:
#                 if 'Laptop section' in q[1]:
#                     writer.writerow(q)
#==============================================================================
import math
def square_check(number):
    for i in range(number+1):
        if i == math.sqrt(number):
            return True
    return False
    
def list_squared(m, n):
    # your code
    f = lambda num: [x for x in range(1, num+1) if num % x == 0]
    pair = []
    for number in range(m, n+1):
        for l in [f(number)]:
            if square_check(sum(l)):
                pair.append([number, sum(l)])

    return pair
    

def longest_palindrome(s):
    pal = []
    for start in range(len(s)):
        for end in range(0,-len(s), -1):
            if end == 0:
                lst = [x for x in s[start:]]
                if lst == list(reversed(lst)):
                    pal.append(len(lst))
            else:
                lst = [x for x in s[start:end]]
                if lst == list(reversed(lst)):
                    pal.append(len(lst))
    return max(pal)

def diamond(n):
    if n >= 0 or n % 2 != 0:  
        string = '\n'.join([' '*((n-num)/2)+'*'*num for num in range(1, n+1, 2) if num !=0])+'\n'
        string += '\n'.join([' '*((n-num)/2)+'*'*num for num in range(n, 0, -2) if num !=n])+'\n'
        return string

import string
def word_score(word):
    d = {' ':0}
    for i, letter in enumerate(string.lowercase):
        d[letter] = i+1
    return sum([d[letter] for letter in word])

def convert(inpt, source, target):
    '''
    Converts between bases. From hex to decimal, etc.
    Args:
        inpt (str): input string. Can be letters or numbers.
        source (str): the starting base. Given as an alphabet.
        target (str): the target base. Given as an alphabet.
    '''
    count = 0
    string = ''
    for i in inpt:
        count *= len(source) 
        count += source.index(i)
    
    while count != 0:
        index = count % len(target) 
        character = target[index] #Gets the character in the target alphabet
        count /= len(target)
        string = character + string
    
    if string != '':
        return string
    else:
        return target[0]



bina      = '01'
octa      = '01234567'
dec       = '0123456789'
hexi      = '0123456789abcdef'
allow     = 'abcdefghijklmnopqrstuvwxyz'
allup     = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha     = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum  = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def testconvert():
    cases = [(("15", dec, bina), "1111"), (("15", dec, octa), "17"), (("1010", bina, dec), "10"), (("1010", bina, hexi), "a"),
             (("0", dec, alpha), "a"),  (("27", dec, allow), "bb"), (("hello", allow, hexi), "320048")]
    test = 1
    for inpt, outpt in cases:
        i, s, t = inpt
        if convert(i, s, t) == outpt:
            print "Test {0} Passed".format(test)
        else:
            print "Test {0} Failed".format(test)
            print convert(i, s, t)
        test += 1

import numpy as np
def stat(strg):
    fmt = 'Range: {0:02d}|{1:02d}|{2:02d} Average: {3:02d}|{4:02d}|{5:02d} Median: {6:02d}|{7:02d}|{8:02d}'
    times = strg.split(',')
    time = [time.strip().split('|') for time in times]
    in_sec = [int(h)*3600 + int(m)*60 + int(s) for h, m, s in time]
    rnge = int(np.ptp(in_sec))
    r = [rnge / 3600, (rnge % 3600) / 60, ((rnge % 3600) % 60)]
    
    med = int(np.median(in_sec))
    m = [med / 3600, (med % 3600) / 60, ((med % 3600) % 60)]
    
    average = int(np.mean(in_sec))
    avg = [average / 3600, (average % 3600) / 60, ((average % 3600) % 60)]
    
    return fmt.format(r[0], r[1], r[2], avg[0], avg[1], avg[2], m[0], m[1], m[2])
    
def autocomplete(input_, dictionary):
    special = '~!@#$%^&*()_+`1234567890-={}|[]\:;<>?,./ '
    inlst = list(input_)
    ind = list(reversed([inlst.index(char) for char in inlst if char in special]))
    for i in ind:
        inlst.remove(inlst[i])
    input_ = ''.join(inlst)       
    lst =[word for word in dictionary if input_.lower() in word.lower()[:len(input_)]]
    if len(lst) >= 5:
        return lst[:5]
    else:
        return lst


def data_reverse(data):
    num = 0
    lst = []
    while num  <= len(data) / 8:
        lst += list(reversed(data[num*8:(num+1)*8]))
        num += 1
    return list(reversed(lst))
    


def test_data_reverse():
    data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
    data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
    if data_reverse(data1) == data2:
        print "Passed"
    else:
        print "Failed"
        print data_reverse(data1)
    data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
    data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
    
    if data_reverse(data3) == data4:
        print "Passed"
    else:
        print "Failed"
        print data_reverse(data3)

def create_square(string, cipher):
    col = {cipher[i]:string[i::5] for i in range(len(cipher))}
    row = {cipher[i]:string[i*5:i*5+5] for i in range(len(cipher))}
    return row, col

def adfgx_encrypt(plaintext, square):
    cipher = 'ADFGX'
    ciphertext = []
    row, col = create_square(square, cipher)
    for letter in plaintext:
        ciphertext += [key for key in row if letter in row[key]]
        ciphertext += [key for key in col if letter in col[key]]
    return ''.join(ciphertext)
    
def adfgx_decrypt(ciphertext, square):
    plaintext = []
    cipher = 'ADFGX'
    row, col = create_square(square, cipher)
    l = [ciphertext[n:n+2] for n in range(0, len(ciphertext), 2)]
    plaintext += [letter for s in l for r, c in s.split() for letter in row[r] if letter in col[c]]              
    return ''.join(plaintext)


def alphabet_war(fight):
    war = {'w':4, 'p':3, 'b':2, 's':1, 
          'm':-4, 'q':-3, 'd':-2, 'z':-1,
          '_':0, '*':0}
    fight = list(fight)
    fight = ['_' if letter not in war else letter for letter in fight ]
    bomb = [i for i, letter in enumerate(fight) if letter == '*']
    for i in bomb:
        if i == 0:
            fight[:i+2] = '_','_'
        else:
            fight[i-1:i+2] = '_','_','_'

    if sum([war[letter] for letter in fight]) > 0:
        return "Left side wins!"
    elif sum([war[letter] for letter in fight]) < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"
    


#==============================================================================
# MAIN METHOD & TESTING AREA
#==============================================================================



def main():
    '''Inside main()'''
    print word_score('word')

  
if __name__ == "__main__":
    main()