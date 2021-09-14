"""
Mad Lib Generator
------------------------
"""
# Bugs are errors - you'll find them with the red squiggly lines

count = 1
while (count < 10):
  # This will ask the user for their answers
  noun = input("Please give me a noun:")
  noun1 = input("Ok, give me another noun:")
  noun2 = input("One more noun:")
  noun3 = input("Ok, last noun: ")
  place = input("Name a place")
  plural_noun = input("Type in a plural noun:")
  adjective = input("gimme an adjective:")
# this is my counter variable, and it will keep track of how many times I loop 
  count = count + 1

  print("--------------------------")
  # concatenation: adding things together 
  print("Be kind to your " + noun + "- you footer" + noun1)
  print("For a duck it may be " + noun2 + ", ")
  print("Be Kind to your " + plural_noun + "in your " + place)
  print("Where the weather is " + adjective + ".")
  print("You may think this is the " + noun3 )
  print("Well it is.")
  print("--------------------------")




# oranges = 0
# while( oranges < 3):
#   print("I bought " + str(oranges) + " oranges")
#   oranges = oranges + 1








