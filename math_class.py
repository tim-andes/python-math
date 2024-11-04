def add(x,y):
    if type(x) or type(y) not in (float, int):
      return TypeError
    else:
       return x + y
    
print(add(1, "one"))