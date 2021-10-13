import turtle
import pandas
from playground import StateWriter
import numpy as np

# setting up the screen
screen = turtle.Screen()
screen.title("U.S.A - Guess the states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# getting data from 50_states.csv file
states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()

points = 0

game_on = True

correct_guessed = []


# turtle writing states setup
writer = StateWriter()

while game_on:
    # user input
    answear_state = screen.textinput(
        title=f"Guess the state {points}/50", prompt="Guess another state: ")

    # if user click cancel
    if answear_state == None:
        game_on = False
    else:
        answear_state = answear_state.title()

    # if user guessed correctly
    if answear_state in states:
        # correct state coordinates
        corect_state = states_data[states_data.state == answear_state]
        state_xcor = corect_state.x
        state_ycor = corect_state.y

        # write state on the map
        writer.write_state(answear_state, state_xcor, state_ycor)

        points += 1
        # getting correctly guessed states in the list
        correct_guessed.append(answear_state)
    else:
        print("Wrong guess")

    # guessed all 50 states
    if points == 50:
        print("Congratulations you have guessed them all!")
        game_on = False

# showing correctly guessed states
print(f"You have guessed:")
for state in correct_guessed:
    print(state)

print(f"And that is {points} of 50 points")
missing_states = np.setdiff1d(states, correct_guessed)

states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv("States to learn.csv")


screen.exitonclick()
