import turtle
import pandas

state = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.screensize(canvwidth=419 ,canvheight=725)
screen.title("State Game")
image = "blank_states_img.gif"
screen.addshape(image)
guess = 0
turtle.shape(image)

size = len(state["state"])
writer = turtle.Turtle()
writer.hideturtle()
guessed_state = []
not_guessed = []

while guess < 50:
  answer = screen.textinput(title=f"{guess}/{size}", prompt="What's another state")
  if answer.lower() == 'exit':
       missing = []
       for state in state["state"]:
            if state not in guessed_state:
                 missing.append(state)
       new_data = pandas.DataFrame(missing)
       new_data.to_csv("missing.csv")
       break
  for i in range(size):
     if answer.lower() == state["state"][i].lower():
         x_axis = state["x"][i]
         y_axis = state["y"][i]
         writer.penup()
         writer.goto(x_axis-10,y_axis)
         writer.write(answer,False,font=("Ariel",7,"bold"))
         guess+=1
         guessed_state.append(guess)






screen.exitonclick()