#Tarea: Empleados
#Juan Guillermo Urincho Tinoco

import datetime
x = datetime.datetime.now()
movs = [[(05, 04, 2017), 165, 500, 'Dep'],[(05, 04, 2017), 240, 900, 'Ext'],[(10, 05, 2017), 124, 600, 'Dep'],
[(10, 05, 2017), 165, 5060, 'Dep'],[(10, 05, 2017), 165, 80,'Ext'],
[(15, 06, 2017), 123, 500, 'Dep'],[(16, 06, 2017), 126, 600, 'Ext']]

#mov=movimiento
#movs=movimientos

def mov(fecha,n_cuenta,monto,tipo,movs):
  fecha = x.day,x.month,x.year
  mov = []
  mov.append(fecha)
  mov.append(n_cuenta)
  mov.append(monto)
  mov.append(tipo)
  movs.append(movimiento)
  print "Movimiento final: ", x.day,"/",x.month,"/",x.year,". ",tipo," de monto: ", monto, ", al N° de cuenta: ", n_cuenta,". Gracias por su preferencia."

def con_dep(movs):
  print "Por favor ingrese las fehas en donde quiera verificar sus movimientos."
  since = raw_input("Ingrese la fecha de inicio en el siguiente formato: dd/mm/aaaa").split("/")
  until = raw_input("Ingrese la fecha de fin en el siguiente formato: dd/mm/aaaa").split("/")
  since_int = tuple([int(i) for i in since])
  until_int = tuple([int(i) for i in until])
  cuenta = []
  total_deps = []
  for mov in movs:
    if since_int[0]==mov[0][0] and since_int[1]==mo[0][1] and since_int[2]==mov[0][2]:
      cuenta.append(movs.index(mov))
    if until_int[2]==mov[0][2] and until_int[1]==mov[0][1] and until_int[0]==mov[0][0]:
      cuenta.append((movs.index(mov)))
  for i in cuenta:
    if mov[3]=='Dep':
      total_deps.append(i)
  print "Estan registrados ", len(total_deps), "depositos en las fechas indicadas."

  def contar_ext(movs):
      print "Por favor ingrese las fechas en donde quiera verificar sus movimientos."
      since = raw_input("Ingrese la fecha de inicio en el siguiente formato: dd/mm/aaaa").split("/")
      until = raw_input("Ingrese la fecha de fin en el siguiente formato: dd/mm/aaaa").split("/")
      since_int = tuple([int(i) for i in since])
      until_int = tuple([int(i) for i in until])
      cuenta = []
      total_exts = []
      for mov in movs:
        if since_int[0]==mov[0][0] and since_int[1]==mov[0][1] and since_int[2]==mov[0][2]:
          cuenta.append(movs.index(mov))
        if until_int[2]==mov[0][2] and until_int[1]==mov[0][1] and until_int[0]==mov[0][0]:
          cuenta.append((movs.index(mov)))
      for i in cuenta:
        if mov[3]=='Ext':
          total_exts.append(i)
      print "Estan registradas ", len(total_exts), "extracciones en las fechas indicadas."

def saldo(movs):
  n_cuenta = int(raw_input("Ingrese el N° de cuenta: "))
  year = int(raw_input("Ingrese el anio: "))
  depositos = []
  retiros = []
  for i in movs:
      if year==mov[0][2] and n_cuenta == mov[1] and mov[3]=='Deposito':
          depositos.append(mov[2])
      elif year==mov[0][2] and n_cuenta == mov[1] and mov[3]=='Extraccion':
          retiros.append(mov[2])
          saldo = sum(depositos)-sum(retiros)
  print "El saldo de la cuenta: ",n_cuenta,", en el anio ", year, ", es de: ", saldo

def main():
  print "Si realizara un Deposito, ingrese 1. Para una Extraccion, ingrese 2."
  tipe = int(input())
  if tipe == 1:
    tipe = "Dep"
    n_cuenta = int(raw_input("Ingrese el numero de cuenta: "))
    monto = int(raw_input("Ingrese el monto: "))
    mov(n_cuenta,monto,tipo,movs)
  else:
    if tipe == 2:
      tipe = "Ext"
      n_cuenta = int(raw_input("Ingrese el numero de cuenta: "))
      monto = int(raw_input("Ingrese el monto: "))
      mov(n_cuenta,monto,tipe,movs)
    else:
      main()
