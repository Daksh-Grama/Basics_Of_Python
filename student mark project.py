import random 

student = ["mark", "sarah", "bob", "elisa", "frank"]
mark = [30, 40, 50, 60, 70]

x1 = random.choice(mark)
x2 = random.choice(student) 
print("{} got {} marks.".format(x2, x1))