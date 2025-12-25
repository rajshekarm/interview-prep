

# # 1 — String Methods
# s = "  Python Is Fun  "

# s.strip()
# s.lower()
# s.replace(" ", "")




# # 2 — Splitting

# s = "apple,banana,grape"

# split_list = s.split(",")
# print(split_list)

# print(('*'.join(split_list)))

#print(s.count('s'))












# # 3. Sliciing
# #Reverse the string using slicing
# # ✅ Correct Ways to Reverse a String
# # ✅ Method 1 — Pythonic (BEST ANSWER)
# # print(s[::-1])


# s = "python"
# n = len(s)
# print(s[n-1:-1:-1])  #s[start : stop : step]
# # Because n is out of bounds and when slicing backwards (-1 step), Python requires start > stop. 
# # Since the start index is invalid, the slice returns an empty string.

# # When step is negative: The slice continues until index > stop, and the stop index is NOT included.


# #Correct version:
# print(s[n-1::-1])