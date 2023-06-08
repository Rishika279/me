"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think this will create a list named "some_words" with the contents: "what", "does", "this", "line", "do", "?". 
some_words = ["what", "does", "this", "line", "do", "?"] 
# I think this will create an iteration that will print one word from the list, "some_words", at a time in order.
for word in some_words: #It printed out each word in the list in order one by one.
    print(word)
# I think this will be similar the the previous code but will print the words under the x variable instead of the word variable.
for x in some_words: #It printed out each word in the list in order one by one.
    print(x)
# I think this will print the whole list, named "some_words".
print(some_words) # It printed "['what', 'does', 'this', 'do', '?']"
#I think this will print "some_words contains more than 3 words" if the number of words in the list, some_words, is greater than 3.
if len(some_words) > 3:
    print("some_words contains more than 3 words") # It printed "some_words contains more than 3 words"

# I think this will define a function that will print information about the current operating system.
def usefulFunction(): #It defined a function to print the current operating system functions.
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

# I think this will put the previous function into effect, printing the current operating system information.
usefulFunction() #It printed the current operating system information.
