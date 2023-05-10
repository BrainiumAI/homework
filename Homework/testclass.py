class Guitar():
    all_guitars = []

    def __init__(self):
        self.numStrings = 6
        self.price = 100
        self.__class__.all_guitars.append(self)

    @staticmethod
    def play():
        print('da da da da!')
    @classmethod
    def discount(cls, amount):
        for guitar in cls.all_guitars:
            guitar.price -= amount
    
    
g = Guitar()
g.play()

class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__()
        self.numStrings = 8
    def use_distortion(self):
        print('using distortion')

eg = ElectricGuitar()
eg.play()
print(eg.numStrings)

eg.use_distortion()
Guitar.discount(77)
date_string = '5/10/2023'
# assign each to diferent variables in a list as a ints, day month year
string_list = ['1', '2', '3', '4', '5']
# ^ cover them to ints. 
day, month, year = date_string.split('/')
print(f'day is {day}. \n {month} is the month, \n and {year} is the year')


ints = [int(x) for x in string_list]


# then lambada square them 
# print(list(map(lambda num: (int(num)**2), string_list)))


numbers = [1, 2, 3, 4, 5]
# print(list(filter(lambda x: x % 2 == 0, numbers)))

# smallest, largest, average = min_max_avg(numbers)
def min_max(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    return min_num, max_num


'''
Great answers! You've shown a solid understanding of the concepts.

Here are ten programming problems that require you to apply the concepts you've learned:



6. **Fibonacci Sequence:** Write a function that generates the Fibonacci sequence up to a certain number. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

7. **Sorting Algorithm:** Implement a sorting algorithm of your choice in Python.

8. **Number to Words:** Write a function that takes an integer and returns its textual representation. For example, if you're given 142, the function should return "one hundred forty two".

9. **Inventory Management:** You have an inventory system where each item has a name, price, and quantity. Implement a system where you can add items, remove items, adjust the quantity of items, and print out the current inventory. Use a class to represent the inventory system and each individual item.

10. **Ciphers:** Implement a Caesar cipher. A Caesar cipher is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.

**Challenge problem:** Implement a tic-tac-toe game where two players can play against each other. You should be able to keep track of the game state, determine when the game is over, and declare the winner. 

Hint: Represent the game board as a 2D list, and use a class to encapsulate the game logic. Implement methods to make a move, check the game state, and declare the winner. This problem will require you to utilize many of the concepts we've covered, including classes, methods, and list manipulation. 

Good luck!

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# make a tuple of the numbers, and a tuple of the letters
def make_tup(lst):
    nums = tuple(filter(lambda x: x is int))
    lets = tuple(filter(lambda x: x is str))
    return nums, lets

'''


# 1. **Palindrome Check:** Write a function that checks if a string is a palindrome. A palindrome is a word that reads the same backward as forward.
def check_palindrome(word):
    wordlist = list(str(word))
    # print(wordlist)
    for char, i in enumerate(wordlist):
        # print(f'char is {char} and i is {i}')
        # print(wordlist[::-1] == wordlist)
        pass

word = 'totally'

check_palindrome(word)

word2 = 'racecar'

check_palindrome(word2)

# 2. **Unique Elements:** Given a list, write a function that returns a new list with unique elements of the first list.
my_list = [1, 2, 2, 2, 4, 5, 6, 5, 6, 8, 9, 7, 4, 5, 919, 4, 2, 2, 4, 3, 5, 6]
unique_list = set(my_list)
# print(unique_list)

# 3. **Multiples of Three and Five:** If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#  The sum of these multiples is 23. Write a function to find the sum of all the multiples of 3 or 5 below a given number.

def multiples(numbers):
    print(f'Number: {numbers}')
    multiple3 = [num for num in numbers if num % 3 == 0]
    multiple5 = [num for num in numbers if num % 5 == 0]
    return sum(set(multiple3+multiple5)) # or no set

def multiples(number):
    numbers = list(range(0, number))
    m3 = [num for num in numbers if num % 3 == 0]
    m5 = [num for num in numbers if num % 5 == 0]
    print(m3, m5)
    return sum(m3 + m5)

print(multiples(5050))

# 4. **String Compression:** Implement a method to perform basic string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3". 
# If the "compressed" string would not become smaller than the original string, your method should return the original string.

# 4. **String Compression:** Implement a method to perform basic string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3". 
# This function should correctly compress the string, as requested. You can test it with the string "aabcccccaaa", and it should return "a2b1c5a3".
# If the "compressed" string would not become smaller than the original string, your method should return the original string.

# test_str = "aabcccccaaa"

# def strcomp(strng):
#     new_str = ''
#     for index, char in enumerate(strng):
#         print(f'char: {char} at index {index}')
#         print(f'The character at index +1 is {strng[index+1]} at index {index+1}')
#         if index < len(strng) - 1: # its the last
#             print(f'char at index+1 is {strng[index+1]} at index {index+1}')

# strcomp(test_str)

# 5. **Prime Number:** Write a function that accepts a number and returns True if it's a prime number, False otherwise.


def is_prime(num):
    pass
def prime_number(num):
    return is_prime(num)
