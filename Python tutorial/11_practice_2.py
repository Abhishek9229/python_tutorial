# first question

# name=input("Enter your name \n")
# print("Good morning " + name)

# second question 

letter = ''' Dear <|name|>,
you are selected!
Have a great day ahead!
we are waiting for you!

Date: <|date|>'''

name = input("Enter you name")
date = input("Enter the date")
letter=letter.replace("<|name|>", name)
letter=letter.replace("<|date|>", date)
print(letter)
