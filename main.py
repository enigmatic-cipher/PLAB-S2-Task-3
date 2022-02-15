"""
Given n as input. Print following pattern using For loop.
Input-> n = 2
Output-> 
**1 
**1**2
"""

def Pattern(n):
  new_string = ""
  for i in range(1,n+1):
    new_string = new_string + str("*"*n) + str(i)
    print(new_string)

num = int(input("Enter number to generate pattern: "))
Pattern(num)

