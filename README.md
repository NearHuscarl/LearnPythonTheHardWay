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
$ python <filename>.py first 2nd 3rd
The script is called: <filename>.py
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
$ Hi near, I'm the <filename>.py script.
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
$ python <filename>.py Exe15_sample.txt
Here's your file 'Exe15_sample.txt': 
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
$ python <filename>.py test.txt
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
