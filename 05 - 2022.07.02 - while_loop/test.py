# Python program to print 
# green text with red background 

# pip install termcolor
# pip install colorama

from colorama import init
from termcolor import colored

init()

print(colored('Hello, World!', 'green', 'on_red')) 