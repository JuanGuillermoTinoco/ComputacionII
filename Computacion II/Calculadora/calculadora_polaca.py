class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def calculadora_polaca(elementos):
    p = Stack()
    for elemento in elementos:
        print ">>>", elemento
        try:
            numero = float(elemento)
            p.push(numero)
        except ValueError:
            if elemento not in "+-*/" or len(elemento) !=1:
                raise ValueError("Operador no es valido")
            try:
                a1 = p.pop()
                print ">>>",a1
                a2 = p.pop()
                print ">>>",a2
            except ValueError:
                raise ValueError("Faltan operandos")

        if elemento == '+':
            resultado = a1 + a2
        elif elemento == '-':
            resultado = a1 - a2
        elif elemento == '*':
            resultado = a1*a2
        elif elemento == '/':
            resultado = a1 / a2
        elif elemento == '%':
            resultado = a1 % a2
    print resultado
    p.push(resultado)
    res = p.pop()
    if p.isEmpty():
        return res
    else:
        print "Error: Pila no vacia"
        raise ValueError("Sobran operandos")

def main():
    expression = raw_input("Ingrese la expresion a evaluar: ")
    elementos = expression.split()
    print calculadora_polaca(elementos)
