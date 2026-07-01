from qiskit import QuantumCircuit
import random

def apply_shield(qc):
    """Charlie (The Aegis) wraps Alice's bit in a 3-qubit shield."""
    # We take the bit Alice put on qubit 0 and spread it to 1 and 2
    qc.cx(0, 1)
    qc.cx(0, 2)
    return qc

def simulate_noise(qc):
    """Simulates random 'Quantum Noise' flipping a bit."""
    if random.random() < 0.3:
        target = random.randint(0, 2)
        qc.x(target)
    return qc

def majority_vote_correction(qc):
    """The magic logic that fixes the flipped bit."""
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.ccx(2, 1, 0) 
    return qc