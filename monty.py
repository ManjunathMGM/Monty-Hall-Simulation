import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')  # dark mode

simulations = 1000000
stay_wins = 0
switch_wins = 0

for _ in range(simulations):
    options = ['goat', 'goat', 'goat']
    car_position = random.randint(0, 2)
    options[car_position] = 'car'

    mychoice = random.randint(0, 2)
    # Remaining doors with 'goats' after Monty opens one door
    remaining_options = [i for i in range(3) if i != mychoice and options[i] == 'goat']
    opened_door = random.choice(remaining_options)
    # The door which isn't my choice and not which Monty opened
    switch_option = next(i for i in range(3) if i != mychoice and i != opened_door)

    if options[mychoice] == 'car':        # Initial Choice win
        stay_wins += 1
    if options[switch_option] == 'car':   # Switched Choice win
        switch_wins += 1

total_wins = stay_wins + switch_wins
# Simulated Probabilitys
print(f"Simulated Probability of winning when staying: {(stay_wins / total_wins) * 100}%")
print(f"Simulated Probability of winning when switching: {(switch_wins / total_wins) * 100}%")

# Theoretical Probabilitys
stay_probability = ((1 / 3) * 100)
switch_probability = ((2 / 3) * 100)

print(f"Theoretical probability of winning when staying: {stay_probability: .4f}%")
print(f"Theoretical probability of winning when switching: {switch_probability: .4f}%")

# Creating a bar chart
labels = ['Simulated-Stay', 'Simulated-Switch', 'Theoretical-Stay', 'Theoretical-Switch']
probabilities = [(stay_wins / total_wins) * 100, (switch_wins / total_wins) * 100, stay_probability, switch_probability]

plt.bar(labels, probabilities, color=['#1f77b4', '#ff7f0e', '#1f77b4', '#ff7f0e'])
plt.ylabel('Probability (%)')
plt.title('Monty Hall Problem Simulation')
plt.ylim(0, 100)

for i, value in enumerate(probabilities):
    plt.text(i, value + 2, f"{value:.2f}%", ha='center', va='bottom', color='white')

plt.show()
