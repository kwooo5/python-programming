my_city = "'New York'"
print(type(my_city))

#Single quotes have exactly
#the same use as double quotes
my_city = 'New York'
print(type(my_city))

#Setting the variable type explicitly
my_city = str("New York")
print(type(my_city))

word1 ='New '
word2 = 'york'
print(word1 + word2)

#how to select the characters
word = 'Rio de Janeiro'
charD = word[7]
print(charD)

#  how to replace part of strings 
word = 'Rio de Janeiro'
x = word.replace('Rio', 'mar')
print(word)

# wordcount 
word = 'Rio de Janeiro'
print(word.count('e'))

# replace 
print(word*3)

# splitting the string 
work = 'Rio de Janeiro'
split_word = work.split('')
print(split_word)
print(split_word(0))