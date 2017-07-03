#Tarea: Empleados.
#Juan Guillermo Urincho Tinoco

class Stack():
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

#adt= area del trabajador
#Task = Tarea del trabajador
#Employee= Empleado

class Task:
	def __init__(adt,description):
		self.adt=adt
		self.description=description
	def __repr__(self):
		return self.description
class tasks_employees:
	def __init__(self):
		self.list_employees=[]
	def add employee(self):
		self.append(Stack())
	def add_task(self,tarea,descripcion):
		self.list_employees[self.list_employees.index(min(self.list_employees))].push(Task(adt,description))
	def process(self):
		for i in range(14,29):
			try:
				while self.list_employees[i].isEmpty()==False:
					t=self.list_employees[i].pop
					print 'Empleado '+str(i+1)+t
			except:
				print 'No hay mas empleados'
				return False
