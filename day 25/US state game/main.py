import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "US state game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("US state game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    )
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer_state]
        t.goto(int(state.x), int(state.y))
        t.write(f"{answer_state}", False, align="center", font="Arial")
        print(answer_state)
        # print(data[data.state == answer_state.capitalize()])
    else:
        print("That state doesn't exist")


screen.exitonclick()
