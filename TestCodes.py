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
import turtle
import random
import csv
import numpy as np



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
    print(arr0)

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
            file_name_1 = input("Enter the file name containing the dictionary: ")
            with open(file_name_1, 'rb') as f:
                dictionary = f.read().split()
                file_name_2 = input("Enter the output file name: ")
                with open(file_name_2, 'wb') as out_file:
                    for word in dictionary:
                        for i in range(len(word)):
                            if word[:i] in dictionary and word[i:] in dictionary:
                                num_compound += 1
                                comp_word = (word + ' = ' + word[:i] + ' + ' + word[i:] + '\n')
                                out_file.write(str(comp_word))
                    out_file.write(str(num_compound))     
                
        except IOError:
            print("This file does not exist")
            valid = True



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
            print("Test {0} Passed".format(test))
        else:
            print("Test {0} Failed".format(test))
            print(convert(i, s, t))
        test += 1


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
        print("Passed")
    else:
        print("Failed")
        print(data_reverse(data1))
    data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
    data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
    
    if data_reverse(data3) == data4:
        print("Passed")
    else:
        print("Failed")
        print(data_reverse(data3))

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
    

def get_int_in_range(low,high):
     prompt = int(input("Enter an integer between max and min"))
     print(prompt)
#     low = int(low)
#     high = int(high)
     if prompt < low:
          print("Integer too low")
          return low
     elif prompt > high:
          print("Integer too high")
          return high
     else:
          print("Good job! You were right")
          return prompt 



class Human:
    def __init__(self, Man, Woman):
        self.Man = Man
        self.Woman = Woman
        
    

class Man(Human):
    def __init__(self, obj):
        Human.__init__(Human.Man("Adam"))

class Woman(Human):
    def __init__(self):
        Human.__init__("Adam", "Eve")

def char_hist(d, string):
    for i in string:
        d[i] = d.get(i, 0) + 1

def check_sum(lst):
    '''This function finds the sum of a given list and checks it 
    against the built-in sum function
    Args:
        lst (list): list of values
    Returns:
        works (bool): either True or False'''
    sum = 0
    for item in lst:
        sum += item
    builtin_sum = sum(lst)
    works = sum == builtin_sum
    return works

    
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    
    def find_area(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
        print('The area of the triangle is {0:0.2f}'.format(area))

    def find_angle(self, a, b):
        self.side_dict = {i+1: side for i, side in enumerate(self.sides)}
        import math
        angle = math.atan2(self.side_dict[a], self.side_dict[b]) * 180/math.pi
        print("The angle between side {0} and side {1} is {2:0.2f} degrees".format(a, b, angle))

def EoS_scores(filein, fileout, section):
    with open(filein, 'r') as fin:
        with open(fileout, 'w') as fout:
            header = fin.readline()
            fout.write(header)
#            reader = csv.reader(fin)
#            writer = csv.writer(fout)
            for q in fin:
                q = q.strip()
#                print(q)
                if section in q:
#                    q[-1] = q[-1].strip()
#                    writer.writerow(q)
                    fout.write(q+'\n')
                    
iv_tests = {1: {'r': -4, 'b': 0.5, 'f': 4, 'i': 0.5, 'desc': 'Invalid rabbits', 'e': 'nan'},
            2: {'r': 4, 'b': 0.5, 'f': -4, 'i': 0.5, 'desc': 'Invalid foxes', 'e': 'nan'},
            3: {'r': 4, 'b': -0.5, 'f': 4, 'i': 0.5, 'desc': 'Invalid birth rate - low', 'e': 'nan'},
            4: {'r': 4, 'b': 1.5, 'f': 4, 'i': 0.5, 'desc': 'Invalid birth rate - high', 'e': 'nan'},
            5: {'r': 4, 'b': 0.5, 'f': 4, 'i': -0.5, 'desc': 'Invalid invalid interaction constant - low', 'e': 'nan'},
            6: {'r': 4, 'b': 0.5, 'f': 4, 'i': 1.5, 'desc': 'Invalid invalid interaction constant - high', 'e': 'nan'}}

v_tests = {7: {'r': 4, 'b': 0.5, 'f': 4, 'i': 0.5, 'desc': 'Valid values, testing calculation', 'e': 0},
           8: {'r': 10, 'b': 0.25, 'f': 2, 'i': 0.75, 'desc': 'Valid values, testing calculation', 'e': 0},
           9: {'r': 10, 'b': 0.75, 'f': 2, 'i': 0.25, 'desc': 'Valid values, testing calculation', 'e': 12},
           10: {'r': 4, 'b': 0.5, 'f': 0, 'i': 0.5, 'desc': 'Valid values, testing calculation', 'e': 6}}

def test_rf():
    mdeduct = '\n[-1] '
    rdeduct = '\n[-0.5] '
    base = 'Test {0} {1}'
    imess = '\nDid not display an appropriate message for invalid argument.'
    plist = '\nrabbits: {2}   birth rate: {3}   foxes: {4}   constant: {5}'
    res = '\nExpected return value:  {6}\nActual return value:  {7}\n\n'
    mfail = base + imess + plist + res
    rfail = base + plist + res
    ks = sorted(iv_tests.keys())
    pts = 0
    for k in ks:
        t = iv_tests[k]
        act = rabbits_with_foxes(t['r'], t['b'], t['f'], t['i'])
        mpass = input('{0} error message displayed? (y/n):  '.format(t['desc']))
        if str(act) == t['e'] and mpass.lower() == 'y':
            print(base.format(k, 'PASSED'))
            pts += 1.0
        elif str(act) != t['e'] and mpass.lower() == 'y':
            print(rdeduct + rfail.format(k, 'failed', t['r'], t['b'], t['f'], t['i'], t['e'], act))
            pts += 0.5
        elif mpass.lower() == 'n' and str(act) == t['e']:
#            print imess
            print(mdeduct + mfail.format(k, 'failed', t['r'], t['b'], t['f'], t['i'], t['e'], act))
        else:
#            print imess
            print(mdeduct + mfail.format(k, 'failed', t['r'], t['b'], t['f'], t['i'], t['e'], act))
    ks = sorted(v_tests.keys())
    for k in ks:
        t = v_tests[k]
        act = rabbits_with_foxes(t['r'], t['b'], t['f'], t['i'])
        if act == t['e']:
            print(base.format(k, 'PASSED'))
            pts += 1.0
        else:
            print(mdeduct + rfail.format(k, 'failed', t['r'], t['b'], t['f'], t['i'], t['e'], act))
    print('Total score: {0}/10.0'.format(pts))

#def rabbits_with_foxes(rabbits, rabbit_birth, foxes, interaction_const):
#    if rabbits < 0:
#        print('ERROR: ', rabbits, 'is an invalid number of rabbits')
#        return float('nan')
#    elif foxes < 0:
#        print('ERROR: ', foxes, 'is an invalid number of foxes')
#        return float('nan')
#    elif rabbit_birth < 0.0 or rabbit_birth > 1.0:
#        print('ERROR: ', rabbit_birth, 'is an invalid rabbit birth rate')
#        return float('nan')
#    elif interaction_const < 0.0 or interaction_const > 1.0:
#        print('ERROR: ', interaction_const, 'is an invalid interaction constant')
#        return float('nan')
#    else:
#        return max(0, int(rabbits+(rabbit_birth * rabbits) - (interaction_const * rabbits * foxes)))

def rabbits_with_foxes(rabbits,rabbit_birth,foxes,interaction_const):
    if rabbits<0:
        print(str(rabbits) + ' is an invalid number of rabbits')
    elif foxes<0:
        print(str(foxes) + ' is an invalid number of foxes')
    elif interaction_const>1.0:
        print(str(interaction_const) + ' is out of bounds for the interaction_const')
    else:    
        nan=rabbits+(rabbit_birth*rabbits)-(interaction_const*rabbits*foxes)
        return float(nan)

def product_of_squares(n):    
    total = 1
    if n > 0:
        count = 0 
        while count < n:
            product = (count+1)**2
            total = product*total
            count += 1 
    else:
        return 0 
    return total


#def find_all(char, string):
#    return [i for i, e in enumerate(string) if e == char]

find_all = lambda char, string: [i for i, e in enumerate(string) if e == char]

                                 
def average_for(integer):
    return sum([float(input("Enter a value: ")) for i in range(integer)])/integer

def remove_vowels(string):
    return ''.join([i  for i in string if i not in ['a', 'e', 'i', 'o', 'u']] )

def reverse_lookup(d, value):
    return ''.join([k for k in d.keys() if d[k] == value])

    
def generate_kv_strings(d):
    return ['{0}: {1}'.format(k, v) for k, v in d.items()]

def count_spaces(filename):
    with open(filename, 'r') as fin: return len(fin.read().split(' ')) - 1

def file_to_dictionary(filename):
    with open(filename, 'r') as fin:
        return {i+1: line.strip() for i, line in enumerate(fin)}


def convert_txt(filename):
    import csv
    with open(filename, 'r') as fin:
        with open("TrafficData4.csv", 'w') as fout:
            csv.writer(fout)
            for line in fin:
                if '  ' in line:
                    line = line.replace('  ', ' 0')
                fout.write(','.join(line.strip().split(' '))+'\n')
import numpy
def array_validation(minimum, maximum, arr):
    """
    determines if all elements in an array are in the range and none zero
    Args:
        minimum(int): the bottom of the range
        maximum(int): the top fo the range
        arr(array): the array to check
    Return:
        (boolean): true if all values are in the range
    """
    min_value = numpy.min(arr)
    max_value = numpy.max(arr)
    if(min_value < minimum) | (max_value > maximum)| (numpy.all(arr) == False):
        return False
    return True

def find_prime(num):
    i = 2
    factors = 0
    while i < num:
        if num % i == 0:
            print(str(i) + ' times '+ str(num/i) + ' is ' + str(num))
            factors += 1
        i += 1
    if factors == 0:
        print(str(num) + ' is a prime number')
    else:
        print(str(num) + ' is not a prime number.')
        print(str(num) + ' has ' + str(factors) + ' number of factors.')

def find_factors(num):
    if [i for i in range(2,num) if num % i == 0] == []:
        print('{} is a prime number'.format(num))
    else:
        print('\n'.join(['{0} times {1} is {2}'.format(x, num/x, num) for x in [i for i in range(2,num) if num % i == 0]]))
        print('{0} has {1} number of factors'.format(num, len([i for i in range(2,num) if num % i == 0])))

def remove_consonants(string):
    return ''.join([i  for i in string if i in ['a', 'e', 'i', 'o', 'u']] )

def fun(t, e, i):
    ret = t[:i]
    ret.append(e)
    return t[i:] + ret

def caesar_cipher(phrase, shift):
    d = {' ': ' '}
    letters = string.lowercase
    cipher = letters[shift:] + letters[:shift]
    for word in phrase.split():
        for i in word:
            d[i] = cipher[letters.find(i)]
    
def usp_pres_worth(A, i, n):
    return A*(((1+i)**n-1)/(i*(1+i)**n))


import colorama; colorama.init(autoreset = True)
from colorama import Fore, Style

class colored():
    """ Changes color of text string in terminal. """
    def red        (self, string): return Style.BRIGHT + Fore.RED     + '{}'.format(string)
    def green      (self, string): return Style.BRIGHT + Fore.GREEN   + '{}'.format(string)
    def yellow     (self, string): return Style.BRIGHT + Fore.YELLOW  + '{}'.format(string)
    def blue       (self, string): return Style.BRIGHT + Fore.BLUE    + '{}'.format(string)
    def purple     (self, string): return Style.BRIGHT + Fore.MAGENTA + '{}'.format(string)
    def cyan       (self, string): return Style.BRIGHT + Fore.CYAN    + '{}'.format(string)
    def white      (self, string): return Style.BRIGHT + Fore.WHITE   + '{}'.format(string)
c = colored()

def test_func():
    print("Hello World")

def lottery(a,b,c):
    if a==b and a==c:
        return 100
    elif a==b or b==c or a==c:
        return 10
    else:
        return 0



def covariance(X,Y):
    mean1 = np.mean(X)
    mean2 = np.mean(Y)
    n = len(X)
    total = 0
    for i in range(n):
        total += ((X[i]-mean1)*(Y[i]-mean2))
    cov = total/(n-1)
    return cov
    
      



#==============================================================================
# MAIN METHOD & TESTING AREA
#==============================================================================
def main():
    '''Inside main()'''
#    print find_all('a', 'banana')
#    print average_for(5)
#    print 'asdfasdfasdfasdf'.count('a')
#    print file_to_dictionary('bullshit.txt')
#    EoS_scores('EoS2020.csv', '201.csv', 'Section 201')
#    EoS_scores('EoS2020.csv', '202.csv', 'Section 202')
#    EoS_scores('EoS2020.csv', '203.csv', 'Section 203')
#    EoS_scores('EoS2020.csv', '204.csv', 'Section 204')
#    print remove_consonants('facetiously')
#    caesar_cipher('this is a phrase', 10)
    
if __name__ == "__main__":
    main()