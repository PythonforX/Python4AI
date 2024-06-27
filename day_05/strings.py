str1 = 'hello rohit how are you'
str2 = "World"
str3 = '''Rohan'''

# # Concatenation
result = str1 +" "+ str2
print(result)

# # Repetition
result = str1 * 3
print(result)

# #Length
len_str = len(str1)
print(len_str)

#Slicing
print(str1[2:4])

#Methods
# upper(), lower(), capitalise
str_upper = str1.capitalize()
print(str_upper)

print(len(str1.strip()))

#split
words = str1.split(" ")
print(words)

#join
joined_word = " ".join(words)
print(joined_word)



