# set practice

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)
print('pineapple' in basket)

a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)

print(a-b)
print(a|b)
print(a&b)
print(a^b)

c = {x for x in 'bghhakektsxs' if x not in 'has'}
print(c)