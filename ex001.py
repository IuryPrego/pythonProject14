coord = ['x', 'y', 'z']
fr = []
f2 = []
f1 = []

for i in range(0, 3):
    f1.append(int(input(f'Digite a coordenada {coord[i]} do vet 1: ')))
for i in range(0, 3):
    f2.append(int(input(f'Digite a coordenada {coord[i]} do vet 2: ')))

for j in range(0, 3):
    fr.append(f1[j] + f2[j])
print(fr)
