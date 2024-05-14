import math 
def transform_numbers(numbers):
    transformed_numbers=[]
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")
    if not numbers:
        return transformed_numbers
    for num in numbers:
        transformed_num=math.sqrt(abs(num))
        transformed_numbers.append(transformed_num)
    return transformed_numbers

input_str = input("Enter elements of the list separated by space: ")
input_numbers=[float(num) for num in input_str.split()]
output_numbers= transform_numbers(input_numbers)
print("Input String of numbers:", input_numbers)
print("Transformed numbers:", output_numbers)
    
        
        
        
    