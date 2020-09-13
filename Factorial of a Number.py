#factorial of a number
#defining a function
def fact(n):
  if n==1:
    return 1
  else:
    return (n*fact(n-1))#function calling it self with an operation

print(fact(5))