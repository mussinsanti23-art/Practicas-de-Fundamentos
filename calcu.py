def sumar(a, b):
 return a + b

def restar(a, b):
 return a - b

def main():

 print("=== CALCULADORA EN PYTHON ===")


 numero1 = float(input("Ingrese el primer número: "))
 numero2 = float(input("Ingrese el segundo número: "))

 print("Suma:", sumar(numero1, numero2))
 print("Resta:", restar(numero1, numero2))

 if __name__ == "__main__":
    main()