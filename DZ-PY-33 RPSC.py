import random

comp_rand = ["rock", "paper", "scissors"]


def battle(warrior):
    if warrior == "rock":
        comp_hero = comp_rand[random.randint(0, 2)]
        if comp_hero == "paper":
            print("Computer victory!")
        elif comp_hero == "scissors":
            print("Player victory!")
        else:
            print("Draft!")
    elif warrior == "paper":
        comp_hero = comp_rand[random.randint(0, 2)]
        if comp_hero == "rock":
            print("Player victory!")
        elif comp_hero == "scissors":
            print("Computer victory!")
        else:
            print("Draft!")
    else:
        comp_hero = comp_rand[random.randint(0, 2)]
        if comp_hero == "rock":
            print("Computer victory!")
        elif comp_hero == "paper":
            print("Player victory!")
        else:
            print("Draft!")


while True:
    in_put = input("Введите одно из трёх:\n\t\tRock\n\t\tPaper\n\t\tScissors\n::  ")
    battle(in_put.lower())
    in_put_2 = input("Хоите продолжть?\n\t\tNo (Нет)\n\t\tВведите что-нибудь другое, например: Нет\n::  ")
    if in_put_2.lower() == "no":
        break
    else:
        continue
