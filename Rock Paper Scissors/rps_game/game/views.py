from django.shortcuts import render
import random

u_points = 0
c_points = 0

def play_game(request):
    global u_points, c_points
    user_choice = request.GET.get('choice')

    if user_choice:
        option = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(option)

        if user_choice == comp_choice:
            result = "It's a tie! 🤝🏻"
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'scissors' and comp_choice == 'paper') or \
             (user_choice == 'paper' and comp_choice == 'rock'):
            result = "Congratulations! You Won!! 🎉"
            u_points += 1
        else:
            result = "Oops! You Lose 😔"
            c_points += 1

        context = {
            'user_choice': user_choice,
            'comp_choice': comp_choice,
            'result': result,
            'u_points': u_points,
            'c_points': c_points,
        }

        return render(request, 'game/index.html', context)

    else:
        return render(request, 'game/index.html', {
            'u_points': u_points,
            'c_points': c_points
        })
