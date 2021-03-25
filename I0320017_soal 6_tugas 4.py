a = 4
b = 11
c = a | b
print("---------- OR -----------")
print('binary dari', a, 'adalah', format(a, '08b'))
print('binary dari', b, 'adalah', format(b, '08b'))
print('binary dari', c, 'adalah', format(c, '08b'))
print("------------------------")

c = a >> b
print("---------- RIGHT SHIFT -----------")
print('binary dari', a, 'adalah', format(a, '08b'))
print('binary dari', b, 'adalah', format(b, '08b'))
print('binary dari', c, 'adalah', format(c, '08b'))
print("----------------------------------")

c = a ^ b
print("---------- XOR -----------")
print('binary dari', a, 'adalah', format(a, '08b'))
print('binary dari', b, 'adalah', format(b, '08b'))
print('binary dari', c, 'adalah', format(c, '08b'))
print("--------------------------")

c = ~a
print("---------- NOT -----------")
print('binary dari', a, 'adalah', format(a, '08b'))
print('binary dari', b, 'adalah', format(b, '08b'))
print('binary dari', c, 'adalah', format(c, '08b'))
print("--------------------------")

c = a & b
print("---------- AND -----------")
print('binary dari', a, 'adalah', format(a, '08b'))
print('binary dari', b, 'adalah', format(b, '08b'))
print('binary dari', c, 'adalah', format(c, '08b'))
print("--------------------------")


