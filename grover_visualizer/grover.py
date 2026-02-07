from math import pi, sqrt, floor

from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import ZGate
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

import animation


def initialize_s(qc, qubits):
    """
    Step 1: Initialization (Superposition)
    Puts all qubits into a superposition of all possible states.
    """
    for q in qubits:
        qc.h(q)

def oracle(n, qc, state='101'):
    """
    Step 2: Oracle
    Marks the target state |101> by flipping its phase.
    Target: q2=1, q1=0, q0=1
    """
    for i in range(len(state)):
        if state[i] == '0':
            qc.x(len(state) - i - 1)
    n_controlled_z(qc, list(range(n)))
    for i in range(len(state)):
        if state[i] == '0':
            qc.x(len(state) - i - 1)

def diffusion(n, qc, qubits):
    """
    Step 3: Diffusion Operator (Inversion about the mean)
    Amplifies the probability of the marked state.
    """
    for q in qubits:
        qc.h(q)
    for q in qubits:
        qc.x(q)
    n_controlled_z(qc, list(range(n)))
    for q in qubits:
        qc.x(q)
    for q in qubits:
        qc.h(q)

def numberOfIterations(N, M):
    """
    Calculate the optimal number of iterations for Grover's algorithm.
    N: Total number of states (2^n for n qubits)
    M: Number of target states
    """
    k=floor((pi/4)*sqrt(N/M))
    return k

def n_controlled_z(qc, qubits):
    n = len(qubits)
    z = ZGate().control(n - 1)
    qc.append(z, qubits)



def main():
    targets=['0101', '1111']  # Target states to search for
    #targets=['101', '110']  # Example with multiple target states
    #targets=['11']

    # Connect to IBM Quantum
    # Note: If you don't have an IBM account configured, this may fail.
    try:
        service = QiskitRuntimeService(channel="ibm_quantum_platform")
        #backend = service.least_busy(operational=True, simulator=False)
        backend = AerSimulator()
    except Exception as e:
        print(f"IBM Quantum connection failed: {e}")
        print("Using local AerSimulator instead.")
        backend = AerSimulator()

    # Create circuit with 3 qubits
    n = len(targets[0])
    qc = QuantumCircuit(n)
    qubits = list(range(n))

    # Apply Grover's Algorithm
    initialize_s(qc, qubits)

    trackStates = []
    state = Statevector.from_instruction(qc)
    for i, amp in enumerate(state.data):
        state.data[i] = abs(amp)**2

    trackStates.append(state)

    for iteration in range(numberOfIterations(pow(2,n), len(targets))):
        for state in targets:
            oracle(n, qc, state)
        diffusion(n, qc, qubits)

        state = Statevector.from_instruction(qc)
        for i, amp in enumerate(state.data):
            state.data[i] = abs(amp)**2

        trackStates.append(state)


    #state = Statevector.from_instruction(qc)
    #for i, amp in enumerate(state.data):
    #    print(f"{i:03b} -> {amp}")


    # STEP 4: Measure
    qc.measure_all()

    animation.startQuantumAnimation(trackStates)
    for i, state in enumerate(trackStates):
        print(f"After iteration {i+1}:")
        for j, amp in enumerate(state.data):
            print(f"{j:0{n}b} -> {amp:.4f}")
        print()

    # Visual representation
    print("Circuit Diagram:")
    print(qc.draw())

    # Execution
    print(f"Running on: {backend.name}")
    qc_transpiled = transpile(qc, backend, optimization_level=3)
    sampler = Sampler(backend)
    job = sampler.run([qc_transpiled], shots=4096)
    print(f"Job ID: {job.job_id()}")
    print("Waiting for results...\n")

    result = job.result()
    # Handle Sampler result format
    counts = result[0].data.meas.get_counts()

    # Display results
    print("Results (State: Count):")
    for state, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{state}: {count} times ({count/4096*100:.1f}%)")

if __name__ == "__main__":
    main()