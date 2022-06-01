def my_function(abcd="default"):
  print("Hello from a function " +str(abcd))

my_function()

def functiontry(*xyz):
    print(len(xyz))
functiontry("abcd","defg")




def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)