colors =['Black','white','green','yellow','orange','red']
color=['navy']
color.extend(colors)
print(colors[2:3])
print(colors[1:5:2])
print(colors[:5])
colors.append('Blue')
colors.insert(2,"Silver")
print(color)
colors[0] = 'Purple'
print(color)
print(colors)
for i in colors:
    if 'Silver' in i:
        print(f"{i} Yes this is silver")
        break
    else:
        print(f"{i} Sorry this not silver this is {i}")
