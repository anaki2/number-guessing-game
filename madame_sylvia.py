import random

cards = [
    {"name": "The Star",    "meaning": "Hope is coming your way. Something you have been wishing for is closer than you think."},
    {"name": "The Moon",    "meaning": "Things are not what they seem. Trust your instincts and pay attention to your dreams."},
    {"name": "The Sun",     "meaning": "Good news is on the way. A happy and confident time is ahead for you."},
    {"name": "The Tower",   "meaning": "A sudden change is coming. It may feel scary, but it will clear the way for something better."},
    {"name": "The Wheel",   "meaning": "Luck is turning in your favor. A new cycle is beginning......go for it!"},
    {"name": "The Hermit",  "meaning": "Take some time alone to think. The answer you are looking for is already inside you."},
    {"name": "The Lovers",  "meaning": "An important choice about a relationship is coming. Follow your heart."},
    {"name": "Strength",    "meaning": "You are stronger than you realize. Stay calm and patient, you will get through this!"},
    {"name": "The Fool",    "meaning": "A fresh beginning is waiting for you. Be brave and take the leap!"},
    {"name": "Justice",     "meaning": "Fairness will win out. A situation that has been unresolved will finally be settled."},
    {"name": "The World",   "meaning": "You are close to finishing something big. Celebrate how far you have come."},
    {"name": "The Empress", "meaning": "A creative and abundant time is ahead. Nurture your ideas and the people you love."},
]

positions = ["Your Past", "Your Present", "Your Near Future", "Your Outcome"]

print("I am Madame Sylvia, and I have chosen a number between the numbers we have which are 12 cards.")
print()
print("Do you dare to read my mind?")
print()

name = input("What is your name? ")
print()
print("Ah, " + name + "... the cards have been waiting for you.")
print()

# Shuffle and pick 12 cards to show
random.shuffle(cards)
available_cards = cards[:12]

print("Here are your 12 face-down cards. Choose 4.")
print()

# Show numbered card backs
for i in range(len(available_cards)):
    print("  [" + str(i + 1) + "] ???")

print()

chosen = []

while len(chosen) < 4:
    pick = input("Pick card number " + str(len(chosen) + 1) + " of 4: ")

    if not pick.isdigit():
        print("Please enter a number.")
        continue

    pick = int(pick)

    if pick < 1 or pick > 12:
        print("Please pick a number between 1 and 12.")
        continue

    if pick in chosen:
        print("You already picked that card. Choose a different one.")
        continue

    chosen.append(pick)
    print("Card " + str(pick) + " chosen!")
    print()

print()
print("Madame Sylvia reveals your reading, " + name + "...")
print("==============================================")
print()

for i in range(4):
    card = available_cards[chosen[i] - 1]
    print(positions[i] + ": " + card["name"])
    print(card["meaning"])
    print()

print("The cards have spoken. May they guide you.")
