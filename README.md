# Quantum Grover's Algorithm with Visualization

This project implements Grover's Algorithm using Qiskit and provides an animation of the probability amplitudes as the algorithm progresses through its iterations.

## Features
- **Grover's Search Algorithm**: Implementation of the quantum search algorithm.
- **Dynamic Oracle**: Configurable target states for the search.
- **State Visualization**: Real-time animation of probability distributions after each iteration.
- **Hybrid Backend Support**: Automatically falls back to local `AerSimulator` if IBM Quantum connection is unavailable.
- **Optimal Iteration Calculation**: Automatically determines the number of iterations needed based on the number of qubits and target states.

## Prerequisites
To run this project, you need Python 3.8+ installed along with the following libraries:
- `qiskit>=1.0.0`
- `qiskit-aer>=0.13.0`
- `qiskit-ibm-runtime>=0.17.0`
- `matplotlib>=3.7.0`
- `numpy>=1.24.0`

## Installation
You can install the package directly from PyPI:
```bash
pip install grover-visualizer
```

Or you can clone the reposetory and isntall the dependencies with:
```bash
gh repo clone SilentSword123456/Groovers_Algorithm-Quantum
cd Groovers_Algorithm-Quantum
pip install -r requirements.txt
```


## Usage
After installation, you can run the visualization using:
```bash
python -m grover_visualizer.grover
```

### Configuration
In `grover_visualizer/grover.py`, you can modify the `targets` list to change the state(s) you are searching for:
```python
targets = ['0101']  # Change this to any bitstring of your choice
```

## Project Structure
- `grover_visualizer/grover.py`: The core script that constructs the quantum circuit, runs the simulation, and manages the algorithm's iterations.
- `grover_visualizer/animation.py`: Contains the logic for the Matplotlib-based animation of quantum states.

## How it Works
1. **Initialization**: The circuit starts by applying Hadamard gates to all qubits, creating a uniform superposition of all possible states.
2. **Oracle**: A phase-flip oracle marks the target state(s) by reversing their signs.
3. **Diffusion (Inversion about the Mean)**: This operator amplifies the probability amplitude of the marked state while decreasing the amplitudes of other states.
4. **Repetition**: The Oracle and Diffusion steps are repeated for the optimal number of times ($\approx \frac{\pi}{4}\sqrt{2^n/M}$).
5. **Animation**: The `grover_visualizer/animation.py` module tracks the statevector after each iteration to visualize how the probability of the target state grows.
6. **Measurement**: Finally, the qubits are measured, and the results are displayed as a histogram of counts.
