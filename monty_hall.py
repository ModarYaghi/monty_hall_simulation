import random
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import stats

sns.set(style='darkgrid')


def monty_hall_sim(num_trials=1000):
    switch_wins = 0
    stay_wins = 0
    switch_win_proba = []
    stay_win_proba = []

    for _ in range(num_trials):
        doors = [0, 0, 1]
        random.shuffle(doors)
        choice = random.choice([0, 1, 2])
        monty_opens = [i for i in range(3) if doors[i] == 0 and i != choice][0]
        switch_choice = [i for i in range(3) if i != choice and i != monty_opens][0]

        if doors[choice] == 1:
            stay_wins += 1
        if doors[switch_choice] == 1:
            switch_wins += 1

        switch_win_proba.append(switch_wins / (switch_wins + stay_wins))
        stay_win_proba.append(stay_wins / (switch_wins + stay_wins))

    return switch_win_proba, stay_win_proba


switch_win_prob, stay_win_prob = monty_hall_sim(10000)

fig, ax = plt.subplots()
ax.set_xlabel('Trials')
ax.set_ylabel('Winning Probability')
ax.set_title('Monty Hall Problem Simulation')
ax.grid(True)
ax.set_ylim([0, 1])
ax.plot([], [], 'g-', label='Switch')
ax.plot([], [], 'r-', label='Stay')
ax.axhline(y=2 / 3, color='g', linestyle='--')
ax.axhline(y=1 / 3, color='r', linestyle='--')
ax.legend()


def update(num):
    ax.clear()
    ax.plot(switch_win_prob[:num], 'g-', label='Switch')
    ax.plot(stay_win_prob[:num], 'r-', label='Stay')
    ax.axhline(y=2 / 3, color='g', linestyle='--')
    ax.axhline(y=1 / 3, color='r', linestyle='--')
    ax.legend()
    ax.set_xlabel('Trials')
    ax.set_ylabel('Winning Probability')
    ax.set_title('Monty Hall Problem Simulation')
    ax.grid(True)
    ax.set_ylim([0, 1])


ani = FuncAnimation(fig, update, frames=len(switch_win_prob), repeat=False)
plt.show()

# Perform a statistical test
t_stat, p_val = stats.ttest_ind(switch_win_prob, stay_win_prob)
print(f"t-statistic: {t_stat}, p-value: {p_val}")
