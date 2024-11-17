import keepdelta as kd



old = (1, 2, 3)
new = (2, 3, 4)
#print(set(list(new)))
delta = kd.create(old, new)
print(delta)
var = kd.apply(old, delta)
print(var)
#print(set([{0: 1, 1: 1, 2: 1}]))
#print('a' != 0)