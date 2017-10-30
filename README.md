# Learn Python the Hard Way 

All Exercises in learnpythonthehardway book

**Link:** https://learnpythonthehardway.org/book/

**Note:** The book in the website use python 2, but these files are written in python 3. There should not be much difference though

### Exercise 1: A Good First Program
```python
print("Hello World!")
print ("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

print('this command will print one line')
print('this\n command\n will\n print\n multiple\n lines')
# print('nevermind')
```
```
Hello World!
Hello Again
I like typing this.
This is fun.
Yay! Printing.
I'd much rather you 'not'.
I "said" do not touch this.
this command will print one line
this
 command
 will
 print
 multiple
 lines
```

### Exercise 2: Comments and Pound Character
```python
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print ("I could have code like this.") # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print ("This will run.")
```
```
I could have code like this.
This will run.
```

### Exercise 3: Numbers and Math
```python
print ("I will now count my chickens:")

print ("Hens", 25 + 30 / 6)
print ("or")
print ("Hens", int(25 + 30 / 6))
print ("Roosters", 100 - 25 * 3 % 4)

print ("Now I will count the eggs:")

print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print ("Is it true that 3 + 2 < 5 - 7?")

print (3 + 2 < 5 - 7)

print ("What is 3 + 2?", 3 + 2)
print ("What is 5 - 7?", 5 - 7)

print ("Oh, that's why it's False.")

print ("How about some more.")

print ("Is it greater?", 5 > -2)
print ("Is it greater or equal?", 5 >= -2)
print ("Is it less or equal?", 5 <= -2)
```
```
will now count my chickens:
Hens 30.0
or
Hens 30
Roosters 97
Now I will count the eggs:
6.75
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2? 5
What is 5 - 7? -2
Oh, that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
```

### Exercise 4: Variables and Names
```python
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")
```
```
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We can transport 120.0 people today.
We have 90 to carpool today.
We need to put about 3.0 in each car.
```

### Exercise 5: More Variables and Printing
```python
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
a_random_floating_point = 3.0

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
print ("Btw here is a floating point: %f." % a_random_floating_point)
print ("Btw here is a floating point: %r" % "haha")
```
```
Let's talk about Zed A. Shaw.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
If I add 35, 74, and 180 I get 289.
Btw here is a floating point: 3.000000.
Btw here is a floating point: 'haha'
```

### Exercise 6: Strings and Text
```python
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print (x)
print (y)

print ("I said %r." % x)
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side"

print (w + e)
```
```
There are 10 types of people
Those who know binary and those who don't
I said 'There are 10 types of people'.
I also said: 'Those who know binary and those who don't'.
Isn't that joke so funny?! False
This is the left side of...a string with a right side
```

### Exercise 7: More Printing
```python
print ("Mary had a little lamp.")
print ("Its fleece was white as %s." % "snow")
print ("And everywhere that Mary went.")
print ("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print (end1 + end2 + end3 + end4 + end5 + end6, end=" ")
print (end7 + end8 + end9 + end10 + end11 + end12)

print (end1 + end2 + end3 + end4 + end5 + end6, end=" - ")
print (end7 + end8 + end9 + end10 + end11 + end12)

print (end1 + end2 + end3 + end4 + end5 + end6, end="")
print (end7 + end8 + end9 + end10 + end11 + end12)

print (end1 + end2 + end3 + end4 + end5 + end6)
print (end7 + end8 + end9 + end10 + end11 + end12)
```
```
Mary had a little lamp.
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese Burger
Cheese - Burger
CheeseBurger
Cheese
Burger
```

### Exercise 8: Printing Printing
```python
formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this things.",
    "That you could type up right.",
    "But it didn't sing.",
    "So i said goodbye."
    ))
```
```
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this things.' 'That you could type up right.' "But it didn't sing." 'So i said goodbye.'
```

### Exercise 9: Printing Printing Printing
```python
# Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print('Here are the days: ', days)
print('Here are the months: ', months)

print("""
There is something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
```
```
Here are the days:  Mon Tue Wed Thu Fri Sat Sun
Here are the months:  Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Nov
Dec

There is something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
```

### Exercise 10: What Was That?
```python
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
```
```
        I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
        * Cat food
        * Fishies
        * Catnip
        * Grass
```

### Exercise 11: Asking Questions
```python
print('How old are you?', end=' ')
age = input()
print('How tall are you?', end=' ')
height = input()
print('How much do you weigh?', end=' ')
weight = input()

print('So, you are %r old, %r tall and %r heavy.' % (age, height, weight))
```
```
How old are you? 38
How tall are you? 6'2"
How much do you weigh? 180lb
So, you are '38' old, '6\'2"' tall and '180lbs' heavy.
```

### Exercise 12: Prompting People
```python
age = input('How old are you? ')
height = input('How tall are you? ')
weight = input('How much do you weigh? ')

print('So, you are %r old, %r tall and %r height' % (age, height, weight))
```
```
How old are you? 38
How tall are you? 6'2"
How much do you weigh? 180lbs
So, you are '38' old, '6\'2"' tall and '180lbs' height
```

### Exercise 13: Parameters, Unpacking, Variables
```python
import sys

script, first, second, third = sys.argv

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)
```
```
$ python exe13.py first 2nd 3rd
The script is called: exe13.py
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd
```

### Exercise 14: Prompting and Passing
```python
from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer))
```
```
$ Hi near, I'm the exe14.py script.
$ I'd like to ask you a few questions.
$ Do you like me near?
$ > Yes
$ Where do you live near?
$ > LA
$ What kind of computer do you have?
$ > quantum

Alright, so you said 'Yes' about liking me.
You live in 'LA'.  Not sure where that is.
And you have a 'quantum' computer.  Nice.
```

### Exercise 15: Reading Files
```python
from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r: " % filename)
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
```
```
$ python exe15.py test15.txt
Here's your file 'test15.txt': 
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

Type the filename again:
> Exe15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
```

### Exercise 16: Reading and Writing Files
```python
from sys import argv

script, filename = argv

print('We are going to erase %r.' % filename)
print('If you dont want that, hit CTRL-C (^C).')
print('If you do want that, hit RETURN')

input('? ')

print('Opening the file...')
target = open(filename, 'w')

print('Truncating the file. Goodbye!')
target.truncate()

print('Now, Im going to ask you for three lines')

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print('Im going to write these to the file.')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
```
```
$ python exe16.py test.txt
We are going to erase 'test.txt'.
If you dont want that, hit CTRL-C (^C).
If you do want that, hit RETURN
? 
Opening the file...
Truncating the file. Goodbye!
Now, Im going to ask you for three lines
line 1: Mary had a little lamb
line 2: It's fleece was white as snow
line 3: It was also tasty
Im going to write these to the file.
```

### Exercise 17: More Files
```python
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print('Copy from %s to %s' % (from_file, to_file))

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print('The input file is %d bytes long' % len(indata))

print('Does the output file exist? %r' % exists(to_file))
print('Ready, hit RETURN to continue, CTRL-C to abort.')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('All right, all done.')

out_file.close()
in_file.close()
```
```
--Output--
$ python exe17.py test17_from.txt test17_to.txt
Copy from test17_from.txt to test17_to.txt
The input file is 21 bytes long
Does the output file exist? True
Ready, hit RETURN to continue, CTRL-C to abort.

All right, all done.
```

### Exercise 18: Names, Variables, Code, Functions
```python
# this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print('arg1: %r, arg2: %r' % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print('arg1: %r, arg2: %r' % (arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print('arg1: %r' % arg1)

# this one takes no argument
def print_none():
    print("I got nothin'.")

print_two('Zed', 'Shaw')
print_two_again('Zed', 'Shaw')
print_one('First!')
print_none()
```
```
arg1: 'Zed', arg2: 'Shaw'
arg1: 'Zed', arg2: 'Shaw'
arg1: 'First!'
I got nothin'.
```

### Exercise 19: Functions and Variables
```python
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print('You have %d cheeses!' % cheese_count)
    print('You have %d boxes of crackers!' % boxes_of_crackers)
    print("Man that's enough for a party!")
    print('Get a blanket.\n')


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
```
```
We can just give the function numbers directly:
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket.

OR, we can use variables from our script:
You have 10 cheeses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can even do math inside too:
You have 30 cheeses!
You have 11 boxes of crackers!
Man that's enough for a party!
Get a blanket.

And we can combine the two, variables and math:
You have 110 cheeses!
You have 1050 boxes of crackers!
Man that's enough for a party!
Get a blanket.
```

### Exercise 20: Functions and Files
```python
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print('First lets print the whole file:\n')
print_all(current_file)

print('Now lets rewind, kind of like a tape.')
rewind(current_file)

print('Lets print three lines:')

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
```
```
$ python exe20.py test20.txt
First lets print the whole file:

This is line 1
This is line 2
This is line 3

Now lets rewind, kind of like a tape.
Lets print three lines:
1 This is line 1

2 This is line 2

3 This is line 3
```

### Exercise 21: Functions Can Return Something
```python
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
```
```
Let's do some math with just functions!
ADDING 30 + 5
SUBTRACTING 78 - 4
MULTIPLYING 90 * 2
DIVIDING 100 / 2
Age: 35, Height: 74, Weight: 180, IQ: 50
Here is a puzzle.
DIVIDING 50 / 2
MULTIPLYING 180 * 25
SUBTRACTING 74 - 4500
ADDING 35 + -4426
That becomes:  -4391.0 Can you do it by hand?
```

### Exercise 24: More Practice
```python
print('Lets practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print('This should be five: %s' % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print('With a starting point of: %d' % start_point)
print("We'd would have %d beans, %d jars and %d crates." % secret_formula(start_point))
```
```
Lets practice everything.
You'd need to know 'bout escapes with \ that do 
 newlines and 	 tabs.
--------------

	The lovely world
with logic so firmly planted
cannot discern 
 the needs of love
nor comprehend passion from intuition
and requires an explanation

		where there is none.

--------------
This should be five: 5
With a starting point of: 10000
We'd would have 5000000 beans, 5000 jars and 50 crates.
```

### Exercise 25: Even More Practice
```python
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full setence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
 ```
 ```
$ python
Python 3.6.2 (default, Jul 20 2017, 03:52:27) 
[GCC 7.1.1 20170630] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import exe25
>>> sentence = 'All good things come to those who wait.'
>>> words = exe25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = exe25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> exe25.print_first_word(words)
All
>>> exe25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> exe25.print_first_word(sorted_words)
All
>>> exe25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = exe25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> exe25.print_first_and_last(sentence)
All
wait.
>>> exe25.print_first_and_last_sorted(sentence)
All
who
```

### Exercie 26: Congratulations, Take a Test!

Fix the broken code

```python
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words)
    """Prints the first word after popping it off."""
    word = words.poop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start-point)

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont)


sentence = "All god\tthings come to those who weight."

words = exe26.break_words(sentence)
sorted_words = exe26.sort_words(words)

print_first_word(words)
print_last_word(words)
.print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = exe26.sort_sentence(sentence)
prin(sorted_words)

print_irst_and_last(sentence)

   print_first_a_last_sorted(senence)

```

Solution:

```python
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


sentence = "All god\tthings come to those who weight."

words = exe26_fixed.break_words(sentence)
sorted_words = exe26_fixed.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = exe26_fixed.sort_sentence(sentence)
print(sorted_words)

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)

```

### Exercise 28: Boolean Practice
```python
# True and True
# False and True
# 1 == 1 and 2 == 1
# "test" == "test"
# 1 == 1 or 2 != 1
# True and 1 == 1
# False and 0 != 0
# True or 1 == 1
# "test" == "testing"
# 1 != 0 and 2 == 1
# "test" != "testing"
# "test" == 1
# not (True and False)
# not (1 == 1 and 0 != 1)
# not (10 == 1 or 1000 == 1000)
# not (1 != 10 or 3 == 4)
# not ("testing" == "testing" and "Zed" == "Cool Guy")
# 1 == 1 and not ("testing" == 1 or 1 == 0)
# "chunky" == "bacon" and not (3 == 4 or 3 == 3)
# 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
```
```
$ python
Python 3.6.2 (default, Jul 20 2017, 03:52:27) 
[GCC 7.1.1 20170630] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> True and True
True
>>> False and True
False
>>> 1 == 1 and 2 == 1
False
>>> "test" == "test"
True
>>> 1 == 1 or 2 != 1
True
>>> True and 1 == 1
True
>>> False and 0 != 0
False
>>> True or 1 == 1
True
>>> "test" == "testing"
False
>>> 1 != 0 and 2 == 1
False
>>> "test" != "testing"
True
>>> "test" == 1
False
>>> not (True and False)
True
>>> not (1 == 1 and 0 != 1)
False
>>> not (10 == 1 or 1000 == 1000)
False
>>> not (1 != 10 or 3 == 4)
False
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1 == 1 and not ("testing" == 1 or 1 == 0)
True
>>> "chunky" == "bacon" and not (3 == 4 or 3 == 3)
False
>>> 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
False
```

### Exercise 29: What If
```python
people = 20
cats = 30
dogs = 15

if people < cats:
    print('Too many cats! The world is doomed!')

if people > cats:
    print('Not many cats! The world is saved!')

if people < dogs:
    print('The world is drooled on!')

if people > dogs:
    print('The world is dry!')

dogs += 5

if people >= dogs:
    print('People are greater than or equal to dogs.')

if people <= dogs:
    print('People are less than or equal to dogs')

if people == dogs:
    print('People are dogs.')
```
```
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs
People are dogs.
```

### Exercise 30: Else and If
```python
people = 30
cars = 40
buses = 15

if cars > people:
    print('We should take the cars.')
elif cars < people:
    print('We should not take the cars.')
else:
    print('we can\'t decide.')

if buses > cars:
    print('That\'s too many buses.')
elif buses < cars:
    print('Maybe we could take the buses.')
else:
    print('We still can\'t decide.')

if people > buses:
    print('Alright, let\'s just take the buses.')
else:
    print('Fine, let\'s stay home then.')
```
```
We should take the cars.
Maybe we could take the buses.
Alright, let's just take the buses.
```

### Exercise 31: Making Decisions
```python
print('You enter a dark room with two doors. Do you go through door #1 or door #2?')

door = input('> ')

if door == '1':
    print('There is a giant bear here eating a cheese cake. What do you do?')
    print('1. Take the cake.')
    print('2. Scream at the bear.')

    bear = input('> ')

    if bear == '1':
        print('The bear eats your face off. Good job!')
    elif bear == '2':
        print('The bear eats your leg off. Good job!')
    else:
        print('Well, doing %s is probably better. Bear runs away.' % bear)

elif door == '2':
    print('You stare into the endless abyss at Cthulhu\'s retina.')
    print('1. Blueberries.')
    print('2. Yellow jacket clothespins.')
    print('3. Understanding revolvers yellow melodies.')

    insanity = input('> ')

    if insanity == '1' or insanity == '2':
        print('Your body survives powered by a mind of jello. Good job!')
    else:
        print('The insanity rots your eyes into a pool of muck. Good job!')

else:
    print('You stumble around and fall on a knife and die. Good job!')
```
```
You enter a dark room with two doors. Do you go through door #1 or door #2?
> 1
There is a giant bear here eating a cheese cake. What do you do?
1. Take the cake.
2. Scream at the bear.
> 2
The bear eats your leg off. Good job!
```
