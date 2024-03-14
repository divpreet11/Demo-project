# # Python 3 program to find factorial of given number
# def factorial(n):
	
# 	# single line to find factorial
# 	return 1 if (n==1 or n==0) else n * factorial(n - 1) 

# # Driver Code
# num = 5
# print("Factorial of",num,"is",factorial(num))


import sys

def factorial(n):
    return 1 if n == 1 or n == 0 else n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <number>")
        sys.exit(1)
    
    num = int(sys.argv[1])
    print("Factorial of", num, "is", factorial(num))