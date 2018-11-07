
def fizzbuzz(a, b):
#making sure that our two variable inputs are of data type list    
    if not isinstance(a, list):
        return"Invalid input"
    if not isinstance(b, list):
        return "Invalid input"
      
#Evaluate the combination of two lists
    entry = a+b
#getting the length of the combined lists  
    my_list = len(entry)
#return Fizzbuzz if it is divisible by both 5 and 3  
    if(my_list % 5 == 0 and my_list % 3 == 0):
        return "fizzbuzz"
#Return Buzz if it is divisible by 5
    if (my_list % 5 == 0):
        return "buzz"
#returns Fizz if the combined length of the lists is divisible by 3
    if (my_list % 3 == 0):
        return "fizz"
#defined function returns the length of combined lists
    return len(entry)

if __name__ == "__main__":
#sample data of two list to be evaluated in the fizzbuzz function
 print(fizzbuzz([1, 2, 3], [ ]))
