import turtle

def main():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(4):
        brad.forward(100)
        brad.right(90)

    window.exitonclick()
    
if __name__ == "__main__":
    main()
