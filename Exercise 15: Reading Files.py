from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r: " % filename)
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())

# --Output--
# $ python <filename>.py Exe15_sample.txt
# Here's your file 'Exe15_sample.txt': 
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

# Type the filename again:
# > Exe15_sample.txt
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.
