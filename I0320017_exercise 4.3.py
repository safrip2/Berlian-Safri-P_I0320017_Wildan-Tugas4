x = True
y = False

print('x and y is', x and y)
print('x or y is', x or y)
print('not x is', not x)

z = 7
print(z > 4 or z < 5) # if one is true then the result is true
print(z > 4 and z < 5) # if one is false then the result is false
print(not((z > 4 and z < 5))) #reverse the result
