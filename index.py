# # Python 3 program to find factorial of given number
# def factorial(n):
	
# 	# single line to find factorial
# 	return 1 if (n==1 or n==0) else n * factorial(n - 1) 

# # Driver Code
# num = 5
# print("Factorial of",num,"is",factorial(num))


import os

def factorial(n):
    return 1 if n == 1 or n == 0 else n * factorial(n - 1)

if __name__ == "__main__":
    num_str = os.getenv("NUM")
    if num_str is None:
        print("Environment variable NUM is not set.")
        exit(1)
    
    try:
        num = int(num_str)
    except ValueError:
        print("Invalid value for NUM. Please provide an integer.")
        exit(1)
    
    print("Factorial of", num, "is", factorial(num))
