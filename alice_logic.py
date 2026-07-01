from qiskit import QuantumCircuit
import random

def prepare_message(secret_bit):

    qc = QuantumCircuit(2, 2)

    # =====================================
    # SECRET DATA
    # =====================================

    if secret_bit == 1:
        qc.x(0)

    # =====================================
    # QUANTUM ONE-TIME PAD
    # =====================================

    kx = random.randint(0, 1)
    kz = random.randint(0, 1)

    if kx:
        qc.x(0)

    if kz:
        qc.z(0)

    # =====================================
    # TRAPDOOR = |+>
    # =====================================

    qc.h(1)

    trapdoor_state = "+"

    return qc, kx, kz, trapdoor_state