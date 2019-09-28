i=10
try:
    i=i/0
except:
    print("Error occured")
else:
    print("Noting went wronf")

j=10
try:
    i=i/0
except:
    print("Error occured")
finally:
    print("finally called")