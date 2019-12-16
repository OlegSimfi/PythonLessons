d = {'id-1': 1, 'id-2': 'Test'}
print(d['id-1'])
print(d['id-2'])

a = dict(short='dict', long='dictionary')
print(a)
a['short'] = 234
print(a)

b = dict.fromkeys(['a', 'b'])
print(b)
b['a'] = 7
b['b'] = 88
print(b)

c = {a: a**2 for a in range(7)}
print(c)

person = {'name': {'last_name': 'Иванов', 'first_name': 'Федор', 'middle_name': 'Иванович'}, 'address': ['г. Киев', 'ул. Хрещатик д. 1', 'кв.17'], 'phone': {'home_phone': '77-67-12', 'mobile_phone': '+380-50-777-77-77', 'mobile_phone_2': 'Нет'}}
print(person['name']['last_name'])
print(person['phone']['mobile_phone'])
