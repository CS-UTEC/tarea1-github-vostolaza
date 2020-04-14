def primo(num):
    for i in range(2,int(num/2)):
        if num % i == 0:
            return False
    return True

numero = float(input("Ingrese un numero: "))

if primo(numero):
    print("El numero es primo")
else:
    print("El numero no es primo")