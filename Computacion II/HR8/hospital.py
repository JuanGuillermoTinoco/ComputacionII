#Tarea: Hospital.
#Juan Guillermo Urincho Tinoco

class Doctor:
	def __init__(self,cod_doctor,date,turn_free,turn_busy):
		self.cod_doctor=cod_doctor
		self.fecha_atention=date
		self.turn_free=turn_free
		self.turn_busy=turn_busy
class Diary_medical:
	def __init__(self,specialty,date1,date2):
		self.specialty=specialty
		self.since=date1
		self.until=date2
		self.diary=[]
	def check_turn(self,doctor,date):
		if any(doctor==m.cod_doctor for m in self.diary):
			for m in self.diary:
				if m.cod_doctor==doctor:
					if date>m.date_atention and m.turn_free>0:
						return True
					else:
						return False
				else:
					pass
		else
			return False
