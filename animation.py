import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


matplotlib.use('TkAgg')

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_ylim(0, 1)

states = []
bars = None

def animate(frame):
    currentFrame = frame // 100
    for bar, val,nextVal in zip(bars, states[currentFrame], states[currentFrame + 1]):
        bar.set_height(val-(val-nextVal)*(frame%100)/100)
    return bars

def startQuantumAnimation(input_states):
    global states, bars
    states = input_states
    iterations = len(states)

    """
    maxi=-2
    for state in states:
            maxi = max(maxi, max(state.data))

    ax.set_ylim(0, maxi)
    """

    # Create bars - one for each element in a state
    num_bars = len(states[0])
    x = list(range(num_bars))
    bars = ax.bar(x, [0] * num_bars)
    states.append(states[len(states)-1])

    num_bars = len(states[0])
    n = int(np.log2(num_bars))  # Number of qubits
    labels = [f"|{i:0{n}b}⟩" for i in range(num_bars)]
    ax.set_xticks(list(range(num_bars)))
    ax.set_xticklabels(labels)

    ax.set_xticklabels(labels, rotation=0, fontsize=10)
    plt.tight_layout()

    anim = animation.FuncAnimation(fig, animate, frames=100*iterations, interval=50, repeat=False)
    plt.show()



def main():
    trackStates = []
    element = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    trackStates.append(element)
    element = [-0.1, 0.2, -0.3, 0.4, -0.5, 0.6, -0.7, 0.8]
    trackStates.append(element)
    startQuantumAnimation(trackStates)

if __name__ == "__main__":
    main()