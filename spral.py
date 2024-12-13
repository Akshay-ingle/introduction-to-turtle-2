import turtle    
mn=turtle.Screen()
mn.bgcolor("light blue") 
mn.title("Turtle")
size = 0
while True: 
    for i in range(4): 
        mn.fd(size + 1)
        mn.left(90)
        size = size - 5
    size = size + 1    