from turtle import Screen , Turtle
import numpy as np

class Snake :
    snake=[]

    def __init__(self):
        
        for i in range (0,-40,-20):
            new_turtle=Turtle(shape="square")
            new_turtle.penup()
            new_turtle.goto(i,0)
            self.snake.append(new_turtle)
    
    def move(self):
            for i in range(len(self.snake)-1,0,-1):
                x=self.snake[i-1].xcor()
                y=self.snake[i-1].ycor()
                self.snake[i].goto(x,y)
            self.snake[0].forward(20)
    
    def up(self):
        if self.snake[0].heading()!=270:
            self.snake[0].setheading(90)
    
    def down(self):
       if self.snake[0].heading()!=90:
            self.snake[0].setheading(270)
    def right(self):
        if self.snake[0].heading()!=180:
            self.snake[0].setheading(0)

    def left(self):
        
        if self.snake[0].heading()!=0:
            self.snake[0].setheading(180)    
 
    def increase(self):
        new_turtle=Turtle(shape="square")
        new_turtle.penup()
        x=self.snake[len(self.snake)-1].xcor()
        y=self.snake[len(self.snake)-1].ycor()
        new_turtle.goto(x,y)
        self.snake.append(new_turtle)



class Food :
    def __init__(self) :
        self.food=Turtle()
        self.food.shape("circle")
        self.food.penup()
        self.food.shapesize(0.4,0.4)
        self.food.color("black")
        self.food.speed(0)
        self.refresh()

    def refresh (self):
        x=np.random.randint(-230,230)
        y=np.random.randint(-230,230)
        self.food.goto(x,y)


def endgame(snake,scoretext):
    for i in range(2,len(snake)-1):
        if snake[0].distance(snake[i])<=12:
            scoretext.game_over()
            return True
    if snake[0].xcor()>=240 or snake[0].xcor()<=-240 or snake[0].ycor()>=240 or snake[0].ycor()<=-240:
        scoretext.game_over()
        return True

    return False


class Scoreboread(Turtle):
    def __init__(self) :
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0,230)
        self.write(f"score={self.score}",True,align="center",font=["Arial",12,"normal"])
    
    def scoreing(self):
        self.score+=1
        self.clear()
        self.goto(0,230)
        self.write(f"score={self.score}",True,align="center",font=["Arial",12,"normal"])

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",True,align="center",font=["Arial",22,"normal"])