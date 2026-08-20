pacientes = int(input("Ingrese cuántos pacientes hay: "))

nombres = []
for i in range(pacientes):
    nombre = input(f"Ingrese el nombre del paciente {i+1}: ")
    s1 = input("Ingrese el primer sintoma: ")
    s2 = input("Ingrese el segundo sintoma : ")
    s3 = input("Ingrese el tercer sintoma: ")
    
    filas = [nombre] 
    for j in range(3):
        if j == 0:   
            filas.append(s1)
        elif j == 1:
            filas.append(s2)
        else:
            filas.append(s3)
            
    nombres.append(filas)

for m in range(len(nombres)):
    print(f"Paciente {m+1 :2d}: {nombres[m]} ")