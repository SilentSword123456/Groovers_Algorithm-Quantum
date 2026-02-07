# Quantum Grover's Algorithm with Visualization

This project implements Grover's Algorithm using Qiskit and provides an animation of the probability amplitudes as the algorithm progresses through its iterations.

## Features
- **Grover's Search Algorithm**: Implementation of the quantum search algorithm.
- **Dynamic Oracle**: Configurable target states for the search.
- **State Visualization**: Real-time animation of probability distributions after each iteration.
- **Hybrid Backend Support**: Automatically falls back to local `AerSimulator` if IBM Quantum connection is unavailable.
- **Optimal Iteration Calculation**: Automatically determines the number of iterations needed based on the number of qubits and target states.

## Prerequisites
To run this project, you need Python installed along with the following libraries:
- `qiskit`
- `qiskit-aer`
- `qiskit-ibm-runtime`
- `matplotlib`
- `numpy`

## Installation
You can install the required dependencies using pip:
```bash
pip install qiskit qiskit-aer qiskit-ibm-runtime matplotlib numpy
```

## Usage
Run the main script to start the simulation and visualization:
```bash
python main.py
```

### Configuration
In `main.py`, you can modify the `targets` list to change the state(s) you are searching for:
```python
targets = ['0101']  # Change this to any bitstring of your choice
```

## Project Structure
- `main.py`: The core script that constructs the quantum circuit, runs the simulation, and manages the algorithm's iterations.
- `animation.py`: Contains the logic for the Matplotlib-based animation of quantum states.
- `Quantum Testing.iml`: IntelliJ IDEA project configuration file.

## How it Works
1. **Initialization**: The circuit starts by applying Hadamard gates to all qubits, creating a uniform superposition of all possible states.
2. **Oracle**: A phase-flip oracle marks the target state(s) by reversing their signs.
3. **Diffusion (Inversion about the Mean)**: This operator amplifies the probability amplitude of the marked state while decreasing the amplitudes of other states.
4. **Repetition**: The Oracle and Diffusion steps are repeated for the optimal number of times ($\approx \frac{\pi}{4}\sqrt{2^n/M}$).
5. **Animation**: The `animation.py` module tracks the statevector after each iteration to visualize how the probability of the target state grows.
6. **Measurement**: Finally, the qubits are measured, and the results are displayed as a histogram of counts.
