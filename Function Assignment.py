#1. Write a Python function to find the maximum of three numbers.
def max_of_three_no(a,b,c):
    return max(a,b,c)
print('Max no among 3,4,5 is',max_of_three_no(3,4,5))

#2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sum_of_list(numbers):
    sum1 = 0
    for i in numbers:
        sum1+=i
    return sum1
l = [8,2,3,0,7]
print(sum_of_list(l))

# 3. Write a Python function to multiply all the numbers in a list.

# 	Sample List : (8, 2, 3, -1, 7)
# 	Expected Output : -336

def mult_of_list(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total
list2 = [8,2,3,-1,7]
print(mult_of_list(list2))

# Write a Python function to reverse a string.
# 	Sample String : "1234abcd"
# 	Expected Output : "dcba4321"

def reversed_string(s):
    return s[::-1]
print(reversed_string('1234abcd'))

def reversed_string2(s):
    return ''.join(reversed(s))
print(reversed_string2('1234abcd'))

# Write a Python function to check whether a number falls within a given range.

def range_check(num,start,end):
    if start <= num <= end:
        return "Number is in the range"
    else:
        return "Number is not in the range"
print(range_check(5,1,10))

#6. Write a Python function that accepts a string and counts the number of upper and lower case letters.
	# Sample String : 'The quick Brow Fox'
	# Expected Output :
	# No. of Upper case characters : 3
	# No. of Lower case Characters : 12

def upper_lower_count(s):
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count += 1

        elif i.islower():
            lower_count += 1
    print('No. of Upper case characters :', upper_count)
    print('No. of Lower case characters :', lower_count)

string = 'The quick Brow Fox'
upper_lower_count(string)

# 7. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#
# 	Sample List : [1,2,3,3,3,3,4,5]
# 	Unique List : [1, 2, 3, 4, 5]

def unique_list(sample):
    unique_l = []
    for i in sample:
        if i not in unique_l:
            unique_l.append(i)
    return unique_l
def using_set(sample):
    return list(set(sample))

Sample_List = [1,2,3,3,3,3,4,5]
print(unique_list(Sample_List))
print(using_set(Sample_List))

# 8. Write a Python function that checks whether a passed string is a palindrome or not.
def palindrome_check(word):
  if word == word[::-1]:
    return 'Given input is palindrome'
  else:
    return 'Non palindrome'
word = input('Enter a word, phrase or sequence ')
print(palindrome_check(word))

# 9. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# 	Sample Items : green-red-yellow-black-white
# 	Expected Result : black-green-red-white-yellow
def hyphen_sort(sequence):
    words = sequence.split('-')
    words.sort()
    result = '-'.join(words)
    return result
sequence = 'green-red-yellow-black-white'
print(sequence)
print(hyphen_sort(sequence))

# 10. Write a Python program to detect the number of local variables declared in a function.
def local_variable_count():
    a = 1
    b = 2
    c = 3
    d = 4
    print('Local variable', locals())
    print('Local variable count', len(locals()))
local_variable_count()

#11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
	# Sample Output:
	# 25
	# 48
a = int(input('Enter a number: '))
add15 = lambda x: x + 15
print('After adding 15, result is:', add15(a))

x = float(input('Enter 1st number: '))
y = float(input('Enter 2nd number: '))
mult = lambda x, y: x * y
print('Multiplication of 2 numbers is:', mult(x, y))

# 12. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# 	Sample Output:
# 	Double the number of 15 = 30
# 	Triple the number of 15 = 45
# 	Quadruple the number of 15 = 60
# 	Quintuple the number 15 = 75
def outer_function(multiplier):
  def inner_function(num):
    return num * multiplier
  return inner_function
double = outer_function(2)
triple = outer_function(3)
quadruple = outer_function(4)
quintuple = outer_function(5)
num = int(input('Enter a number: '))
print('Double the number of',num,'=',double(num))
print('Triple the number of',num,'=',triple(num))
print('Quadruple the number of',num,'=',quadruple(num))
print('Quintuple the number of',num,'=',quintuple(num))

# #13. Write a Python program to sort a list of tuples using Lambda.
# 	Original list of tuples:
# 	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# 	Sorting the List of Tuples:
# 	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
data = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_result = sorted(data, key = lambda x : x[1])
print('Sorted result is as below')
print(sorted_result)

#14. Write a Python program to sort a list of dictionaries using Lambda.
	# Original list of dictionaries :
	# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
	# Sorting the List of dictionaries :
	# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

phone_data = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sorted_by_color = sorted(phone_data, key = lambda x : x[2])
print(sorted_by_color)

#15. Write a Python program to filter a list of integers using Lambda.
	# Original list of integers:
	# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# Even numbers from the said list:
	# [2, 4, 6, 8, 10]
	# Odd numbers from the said list:
	# [1, 3, 5, 7, 9]

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda x: x%2==0, given_list))
odd_list = list(filter(lambda x: x%2!=0, given_list))

print('Even number from given list')
print(even_list)
print('Even number from odd list')
print(odd_list)

# 16. Write a Python program to square and cube every number in a given list of integers using Lambda.
# #
# # 	Original list of integers:
# # 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 	Square every number of the said list:
# # 	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # 	Cube every number of the said list:
# # 	[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_list = list(map(lambda x:x**2, given_list))
cube_list = list(map(lambda x:x**3, given_list))
print('Square every number of the said list:')
print(square_list)
print('Cube every number of the said list:')
print(cube_list)

#18. Write a Python program to find if a given string starts with a given character using Lambda.
a = 'hello'
b = 'h'
start_check = lambda x,y:'Start with that character' if x.startswith(y) else 'Not start with given char'
print(start_check(a,b))

# 19. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
#
# 	Original arrays:
# 	[-1, 2, -3, 5, 7, 8, 9, -10]
# 	Rearrange positive and negative numbers of the said array:
# 	[2, 5, 7, 8, 9, -10, -3, -1]
array = [-1, 2, -3, 5, 7, 8, 9, -10]
sorted_array = sorted(array, key= lambda x: x>0, reverse=True)
print(sorted_array)

# 20. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
#
# 	Original arrays:
# 	[1, 2, 3, 5, 7, 8, 9, 10]
# 	Number of even numbers in the above array: 3
# 	Number of odd numbers in the above array: 5

array_eo = [1, 2, 3, 5, 7, 8, 9, 10]
even_list = len(list(filter(lambda x: x%2==0, array_eo)))
odd_list = len(list(filter(lambda x: x%2!=0, array_eo)))
print('Number of even numbers in the above array: ',even_list)
print('Number of odd numbers in the above array: ',odd_list)

# 21. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
#
# 	Orginal list:
# 	[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# 	Numbers of the above list divisible by nineteen or thirteen:
# 	[19, 65, 57, 39, 152, 190]
num_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
divi_list = list(filter(lambda x:x%13==0 or x%19==0,num_list))
print(divi_list)

#22. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
text = input("Enter a string: ")

check = lambda x: (
    any(ch.isupper() for ch in x) and
    any(ch.islower() for ch in x) and
    any(y.isdigit() for y in x) and
    len(x) >= 8
)

print(check(text))