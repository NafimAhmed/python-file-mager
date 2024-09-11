
file=open('init.txt')
content=file.read()
print(content)
file.close()


with open('init.txt') as file:
    content = file.read()
    print(content)


with open('init.txt',mode="a") as file:
    file.write('. I am a coder')

with open('init.txt') as file:
    content = file.read()
    print(content)

with open('new_file.txt',mode='w') as file:
    file.write('this is new erra')

with open('new_file.txt') as file:
    content = file.read()
    print(content)

with open('new_file.txt',mode="a") as file:
    file.write('. I am a coder')