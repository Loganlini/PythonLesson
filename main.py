
# def ginger(deco):
# 	def wrapper():
# 		deco()
# 		print('ginger')
# 	return wrapper

# def hard_worker(deco):
# 	def wrapper():
# 		deco()
# 		print('hard worker')
# 	return wrapper

# def friendly(deco):
# 	def wrapper():
# 		deco()
# 		print('friendly')
# 	return wrapper
  
# def wrinkles(deco):
# 	def wrapper():
# 		deco()
# 		print('wrinkles')
# 	return wrapper

# def freckles(deco):
# 	def wrapper():
# 		deco()
# 		print('freckles')
# 	return wrapper

# def scar(deco):
# 	def wrapper():
# 		deco()
# 		print('scar')
# 	return wrapper
# @friendly
# @hard_worker
# @ginger
# @freckles
# @wrinkles
# @scar
# def human():
# 	print('This is human')

 # human()

# def bread(func):
#     def wrapper():
#         fu
# def sandwich():
#     print('This is sandwich')
# from tkinter import *


# class Main(Frame):
#     def __init__(self, root):
#         super(Main, self).__init__(root)
#         self.build()

#     def build(self):
#         pass
 
#     def logicalc(self, operation):
#         pass

#     def update():
#        pass


# if __name__ == '__main__':
#     root = Tk()
#     root["bg"] = "#000"
#     root.geometry("485x550+200+200")
#     root.title("Калькулятор")
#     root.resizable(False, False)
#     app = Main(root)
#     app.pack()
#     root.mainloop() 

# btns = [
#             "C", "DEL", "*", "=",
#             "1", "2", "3", "/",
#             "4", "5", "6", "+",
#             "7", "8", "9", "-",
#             "+/-", "0", "%", "X^2"
#         ]
# 	def happybirthday(self):
# 		self.age +=1 
# 		print('I am', self.age)
# 	def eat(self):
# 		print('I am eating')

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
 # 		self.end()
 # 		self.is_alive()

 # obj = Student('Bob')
 # univer = University('Step Univer', 'Computer Science')
 # for day in range(365):
 # 	if obj.alive == False:
 # 		break
 # 	obj.live(day)
		
class Fly:
 	def __init__(self, name):
 		self.size = 'Big'
 		self.type = 'Fly'
 		self.food = 'Shit'
 	def eating(self):
 	  print('I can eat')
  def flying(self):
    print('I can fly')