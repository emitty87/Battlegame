characters = ["Goku", "Naruto", "Captain Levy"]
goku = "Goku"
naruto = "Naruto"
captain_levy = "Captain Levy"

goku_hp = 9001  # OVER 9,000!!!!!!!!!!!!!!!
naruto_hp = 2000
captain_levy_hp = 750

goku_damage = 1000
naruto_damage = 600
captain_levy_damage = 1350

villain = "Frieza"
frieza_hp = 7500
frieza_damage = 500

print("1)  Goku")
print("2)  Naruto")
print("3)  Captain Levy")


while True:
    character = input("Choose your Character: ")
    if character == "1":
        character = goku
        print(f"You have chosen the character: {character}")
        my_hp = goku_hp
        my_damage = goku_damage
        print(f"Health: {my_hp}")
        print(f"Damage: {my_damage}")
        break
    if character == "2":
        character = naruto
        my_hp = naruto_hp
        my_damage = naruto_damage
        print(f"You have chosen the character: {character}")
        print(f"Health: {my_hp}")
        print(f"Damage: {my_damage}")
        break
    if character == "3":
        character = captain_levy
        my_hp = captain_levy_hp
        my_damage = captain_levy_damage
        print(f"You have chosen the character: {character}")
        print(f"Health: {my_hp}")
        print(f"Damage: {my_damage}\n")
        break
    else:
        print("Unknown Character\n")
        continue

while True:
    frieza_hp = frieza_hp - my_damage
    print(character, "damaged", villain)
    print("BANG! BANG! BANG!")
    print(f"{villain}'s hitpoints are now: {frieza_hp}\n")
    if frieza_hp <= 0:
        print(villain, "has lost the battle ")
        break

    my_hp = my_hp - frieza_damage
    print(f"{villain} strikes back at {character}")
    print("WHOOOOOOOSH!!")
    print(f"{character}'s hitpoints are now: {my_hp}\n")
    if my_hp <= 0:
        print(f"{character} has lost the battle.")
        break
