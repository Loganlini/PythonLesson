def ask_age():
	num1 = sign = num2 =''
	# sign = ''
	# num2 = ''
	while num1 == '' or sign == '' or num2 == '':
		try:
			num1 = int(input('Input your number 1: '))	
			num2 = int(input('Input your number 2: '))
			sign = input('Input your sign:')
			if sign == '+' or sign == '-' or sign == '*' or sign == '/':
				print(num1,sign,num2)
			else:
				sign = ''
				raise ValueError
		except ValueError:
			print('You need to write normal evaluation')

		if sign == '+':
			print(num1,sign,num2,'=',num1+num2)
		elif sign == '/':
			try:
				print(num1,sign,num2,'=',num1/num2)
			except:
				print('This is division by zero!!!')
		print('The end of program')
# Сделать функцию калькулятор, в которой вы будете вводить два числа и знак. Отловить исключительные ситуации
def ask_age2():
	age = ''
	while age =='':
		age = int(input('Input your age: '))
		print('Your age is', age)
	print('The end of program')

ask_age()



# class Human:
# 	def __init__(self, name):
# 		self.name = name
# 		self.gender = 'None'
# 		self.age = 0
# 	def live(self):
# 		print(self.name, 'is alive')
# 	def happybirthday(self):
# 		self.age +=1 
# 		print('I am', self.age)
# 	def eat(self):
# 		print('I am eating')
# # Создать класс Животное. От него наследуются классы котик, собачка и хомяк.
# # В классе животное есть 3 поля (характеристики) и 2 поведения (методы)
# # В классах конкретных животных нужно добавить еще 1 поведение
# class Parent(Human):
# 	def __init__(self,name):
# 		super.__init__()
# 		self.gender = 'Female'
# 	def work(self):
# 		print(self.name,' can work')
# 		print(f"{self.name} is {self.age}")
# 	def eat(self):
# 		# super().eat()
# 		print('It is apple') # it is what she eats specific

# class Child(Human):
# 	def __init__(self,name):
# 		super.__init__(name)
# 		self.irritiated = 0
# 	def study(self):
# 		self.irritiated+=10
# 		print(self.name,' can study')
# 		if self.irritiated > 30:
# 			print('I want to chill')

# child1 = Child('Bob')



# # child1.study()
# # child1.live()
# # child1.happybirthday()
# # child1.happybirthday()
# # child1.happybirthday()

# parent1 = Parent('Jane')
# child1.eat()
# parent1.eat()
# # parent1.work()
# # parent1.eat()
# # for i in range(30):
# # 	parent1.happybirthday()
# # a = 4
# # print('a')
# # print(a)
# # if a == 5:
# # 	print('if 1')
# # elif a > 3:
# # 	print('if 2')
# # elif a < 6:
# # 	print('if 3')
# # a = 0
# # while a<5:
# # 	print('hi')
# # 	a = a + 1

# # for i in range(5):
# # 	print(i)
# # print('Hello world')
# # print('This is my first commit')

# # class Human:
# # 	def __init__(self):
# # 		self.name = 'None'
# # 		self.age = 0
# # 		self.gender = 'None'
# # 	def introduce(self):
# # 		print('Hello, my name is', self.name)
# # 	def add_info(self):
# # 		self.name = input('Name: ')
# # 		self.age = int(input('Age: '))
# # 		self.gender = input('Gender: ')

# # obj = Human('')
# # obj.introduce()
# # obj.add_info()
# # obj.introduce()

# # from random import *

# # class University:
# # 	def __init__(self, title, faculty):
# # 		self.title = title
# # 		self.faculty = faculty
# # 		self.budget = False;
# # 	def check_progress(self, student):
# # 		if student > 3:
# # 			self.budget = True
# # 		self.isbudget()

# # 	def isbudget(self):
# # 		if self.budget == True:
# # 			print('Congratulation! You are on budget!')

# # class Student:
# # 	def __init__(self, name):
# # 		self.name = name
# # 		self.gladness = 50
# # 		self.progress = 0
# # 		self.alive = True

# # 	def ask_budget(self, university):
# # 		university.check_progress(self.progress)
		
# # 	def study(self):
# # 		print('Study time')
# # 		self.progress += 0.12
# # 		self.gladness -= 5
		
# # 	def sleep(self):
# # 		print('Sleep time')
# # 		self.gladness += 3
		
# # 	def chill(self):
# # 		print('Chill time')
# # 		self.gladness += 5
# # 		self.progress -= 0.1
		
# # 	def is_alive(self):
# # 		if self.progress < -0.5:
# # 			print('Sooo bad')
# # 			self.alive = False
# # 		elif self.gladness <= 0:
# # 			print('Depression...')
# # 			self.alive = False
# # 		elif self.progress > 5:
# # 			print('Passed the exam!')
# # 			self.alive = False
		
# # 	def end(self):
# # 		print('Gladness:', self.gladness)
# # 		print('Progress:', self.progress)
		
# # 	def live(self, day):
# # 		print('Day:',day)
# # 		if day % 10 == 0:
# # 			self.ask_budget(univer)
# # 		live_cube = randint(1,3)
# # 		if live_cube == 1:
# # 			self.study()
# # 		elif live_cube == 2:
# # 			self.sleep()
# # 		elif live_cube == 3:
# # 			self.chill()
# # 		self.end()
# # 		self.is_alive()

# # obj = Student('Bob')
# # univer = University('Step Univer', 'Computer Science')
# # for day in range(365):
# # 	if obj.alive == False:
# # 		break
# # 	obj.live(day)
		