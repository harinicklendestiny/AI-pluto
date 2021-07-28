import os
print("What would you like to add?")
add = input("> ")
add_file = open("movie scripts.txt", 'a')
add_file.write('\n')
add_file.write(add)
add_file.close()