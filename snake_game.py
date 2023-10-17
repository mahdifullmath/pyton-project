from turtle import Screen , Turtle
import time
import snake




screen=Screen()
screen.setup(width=500, height=500)
screen.title("snake")
screen.tracer(0)
snake1=snake.Snake()

screen.update()
screen.listen()
screen.onkeypress(snake1.up,"Up")
screen.onkeypress(snake1.down,"Down")
screen.onkeypress(snake1.left,"Left")
screen.onkeypress(snake1.right,"Right")
food=snake.Food()
score=snake.Scoreboread()
game=True
while game:
    
    snake1.move()
    screen.update()
    time.sleep(0.1)
    if snake1.snake[0].distance(food.food)<=18:
        food.refresh()
        snake1.increase()
        score.scoreing()
    game=not(snake.endgame(snake1.snake,score))

screen.exitonclick()