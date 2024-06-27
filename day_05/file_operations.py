# file = open(filename, mode)

#Read
# with open('pie.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines)

#Write
with open('pie.txt', 'a') as file:
    file.write("\nNew content")
    print("Append operation successfull")