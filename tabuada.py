number = int(input('Digite o número: '))

print(f'\n---Tabúada do {number}---')
for i in range(1, 11):
    print(f'{number} X {i} = {number * i}')
