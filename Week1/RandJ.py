# Leave this list definition as it is
romeo_and_juliet_characters = [
  "Romeo", "Juliet", "Benvolio", "Hamlet", "Rosaline Capulet",
  "Lady Capulet", "Montague", "Lady Montague", "Apothecary", 
  "Mercutio", "Friar Laurence", "Iago", "Tybalt", "Count Paris",
  "Prince Escalus"
]

# Only change code below this line

# Replace Hamlet with Capulet
index1 = romeo_and_juliet_characters.index("Hamlet")
romeo_and_juliet_characters[index1] = "Capulet"

# Replace Iago with Balthasar
index2 = romeo_and_juliet_characters.index("Iago")
romeo_and_juliet_characters[index2] = "Balthasar"

print(romeo_and_juliet_characters)