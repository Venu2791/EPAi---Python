# Session 4 – Test Cases and code understanding
## Qualean Implementation
### Qualean = Boolean+Quantum: 
Qualean class that is inspired by Boolean and Quantum concepts. 
We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. 
The moment we assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. 
## It implements these functions:
We should note here that any number except 0 has a Boolean value of True. This is applicable for all of the below functions.
1)  __and__ : Compares two numbers and gives the result whether it is True or False (Intersection of the results). We have also considered the short circuit here that 
q1 and q2 returns False 
•	when q2 is not defined 
•	q1 is False
So, if the first value is False, no matter what the second value is, the result of this function is False. But we have to note that when q1 is True and q2 is not defined, we have displayed the message Q2 is not defined.
2)  __or__ : Compares two numbers and gives the result whether it is True or False (Union of the results). We have also considered the short circuit here that 
q1 and q2 returns True 
•	when q2 is not defined 
•	q1 is True
So, if the first value is True, no matter what the second value is, the result of this function is True. But we have to note that when q1 is False and q2 is not defined, we have displayed the message Q2 is not defined. 
3)  __str__ : Used for creating output for end user .
4)  __repr__ : Used for debugging and development.
5)  __add__ : Adds two numbers.
6)  __eq__ : Checks is two numbers are equal.
7)  __float__ : Converts the input number into floating type.
8)  __ge__ : Checks if the first number is greater than or equal to the second number.
9)  __gt__ : Checks if the first number is greater than the second number.
10) __invert__ : Changes the sign of the number.
11) __le__ : Checks if the first number is less than or equal to the second number.
12) __lt__ : Checks if the first number is less than the second number.
13) __mul__ : Multiples two numbers.
14) __sqrt__ : Finds the square root of a number. (For negative number, the result is a complex number).
15) __bool__ : Displays the value as True, except for 0.
## Test Cases
1)  README exists
2)  README has at least 500 words
3)  Methods mentioned in README
4)  README file formatting 
5)  Code Indentation and spaces
6)  Function name should be in small letters
7)  All the above 15 functions used
8)  Input should be 0 or -1 or 1
9)  Testing __add__ 
10) Testing __mul__ 
11) Testing __bool__ 
12) Testing __float__
13) Testing __and__
14) Testing __or__
15) Testing __invert__
16) Testing __ge__
17) Testing __gt__
18) Testing __le__
19) Testing __lt__
20) Testing __eq__
21) Testing __sqrt__
22) Testing if q + q + q ... 100 times = 100 * q
23) q.__sqrt__() = Decimal(q).sqrt. We have considered only the positive numbers in this case since Decimal(q).sqrt will throw an error for negative numbers
24) Sum of 1 million different qs is very close to zero using isclose()
25) Short circuit of and/or
