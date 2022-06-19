point = dict(x=1, y=2)
# print(point.get('a', 'Not Found!'))
point['x'] = 10
point['y'] = 20
for key, value in point.items():
    print(key, value)
