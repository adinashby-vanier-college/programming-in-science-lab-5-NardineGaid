# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    shape = ""

    for i in range(1, n+1):

        if i == 1 or i == n:

            shape+= n * "*" + '\n'

        else: 
            shape += '*' + ' ' * (n-2) + '*' + '\n'    
    return(shape.strip())
# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""

    for i in range (1, n + 1):
        for j in range(1, i + 1):
            result += str(j)
        result = result.rstrip()
        result += "\n"
    
    return result.rstrip()

#print(number_pattern(4))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    sum = 0 

    for i in range (1, n + 1): 
        sum += int(i)
    return sum

#print (sum_of_natural_numbers(5))

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = "" 
    
    for i in range(1, n + 1):
        
        spaces = ' ' * (n - i)
        stars = '*' * (1 + 2 * (i-1))
    
        result += spaces + stars + '\n'
    
    return result.rstrip()
   
print (centered_star_pyramid(4))