# #check if string has space

# name = "rajshekar mudigonda"

# print(name.split(" "))

# #get the first name from the name

# firstIdx = name.find(" ")

# firstName = name[0:firstIdx]

# print(firstName)
# # print(name.split(" ")[0])

# #How to split first & last name


#How do u get the last character of s 
s = "python"
n = len(s)
print(s[n:-1:-1])


# #How do you extract only "mudigonda" using slicing?





# #👉 How many times does "s" occur? Write the code.
# s = "mississippi"
# count = 0
# for i in s:
#     if i == 's':
#         count+=1
# print(count)

# print(s.count('s'))


# #check if email is valid?
# email = "rashekarmudigonda@gmail.com"








# # #👉 Write ONE line of Python to:
#     # remove extra spaces
#     # convert to lowercase
#     # store it back in username

# username = " Admin "




# res = ""
# print(len(username))
# for ch in username:
#     if ch != " ":
#         res += ch
# print(res)
# print(username.strip())






# #Print the ASCII value each character
# strr = "after"

# for ch in strr:
#     print(ord(ch))





# #Find the max ASCII value character in the given name and use it as the key for the bucket and group those names together
# names = ["raj", "ramesh", "suresh", "rajesh", "somesh"]

# #Solution
# buckets = {}
# for name in names:
#     prev = ord('a')
#     for ch in name:
#         if ord(ch)>prev:
#             prev = ord(ch)
#     res = str(prev)
#     buckets[res] = name

# print(len(buckets))




        