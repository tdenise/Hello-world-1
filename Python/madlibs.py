"""
This program is a python mad libs
and it takes user input and then is
basically mad libs, in python.
"""
#The template for the story

print ("Mad Libs is starting. Get ready!")
name= input("Enter a name: ")
adj1= input("Enter an adjective: ")
adj2= input("Enter a second adjective: ")
adj3= input("Enter another adjective: ")
verb= input("Enter a verb: ")
non1= input("Enter a noun: ")
non2= input("Enter a noun: ")
animal= input("Enter an animal: ")
food= input("Enter a food: ")
fruit= input("Enter a fruit: ")
superhero= input("Enter a superhero: ")
country= input("Enter a country: ")
dessert= input("Enter a dessert: ")
year= input("Enter a year: ")

STORY= "This morning {} woke up feeling {} \
'It is going to be a {} day!' Outside, a bunch of \
{}s were protesting to keep {} in stores. They began\
to {} to the rhythm of the {}, which made all the\
{}s very {}. Concerned, {} texted {}, who flew {} to {} and\
dropped {} in a puddle of frozen {}. {} woke up in the year\
{}, in a world where {}s ruled the world.".format(name,adj1,adj2,animal,food,verb,non1,fruit,adj3,name,superhero,name,country,name,dessert,name,year,non2)


print (STORY)
