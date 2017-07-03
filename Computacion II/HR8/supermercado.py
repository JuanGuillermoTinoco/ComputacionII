#Tarea: Mercado.
#Juan Guillermo Urincho Tinoco

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

	def suma(self):
		return sum(self.items)

    def size(self):
        return len(self.items)

class Product:
	def __init__(self,cod_product,price,date):
		self.cod_product=cod_product
		self.date=date
		self.price=price
		self.prices_ant=Queue()
	def remark(self,newprice,date):
		self.prices_ant.enqueue(self.price)
		self.price=newprice
		self.date=date
    def change_price(self):
        self.rem_list.enqueue(self.price)
        self.price=Price(int(raw_input('Precio del producto: ')),datetime.date(*map(int,raw_input('Fecha: ').split())))
        self.rem_number+=1
	def average(self):
		average=(float(self.price+self.prices_ant.sum())/float(1+self.prices_ant.size()))
		return average
class Products_remarked:
	def __init__(self):
		self.products=[]
	def add_product(self,cod_product,price,date):
		self.products.append(Product(cod_product,price,date))
		self.products=sorted(self.products,key=lambda x: (x.cod_product,x.prices_ant.size(),x.average()))
	def remarked_product(self,cod_product,newprice,date):
		if any(i.cod_product==cod_product for i in self.products):
			for pro in self.products:
				if pro.cod_product==cod_product:
					pro.remarked(newprice,date)
					return True
				else:
					pass
		else:
			return False
	def products_more_remarked(self,n):
		products_more=[]
		for pro in self.products:
			if pro.prices_ant.size()>n:
				products_more.append(pro)
			else:
				pass
