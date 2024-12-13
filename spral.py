import turtle  

mn=turtle.Screen()
mn.bgcolor("light blue") 
mn.title("Turtle")
size = 0
mg=turtle.Turtle()
while True: 
    for i in range(4): 
        mg.fd(size + 1)
        mg.left(90)
        size = size - 5
    size = size + 1    