from qiskit_aer import AerSimulator
from qiskit import transpile

def run_server(qc):

    simulator = AerSimulator()

    # =====================================
    # RESTORE HADAMARD BASIS
    # =====================================

    qc.h(1)

    # =====================================
    # FINAL MEASUREMENT
    # =====================================

    qc.measure_all()

    compiled = transpile(qc, simulator)

    result = simulator.run(
        compiled,
        shots=1024
    ).result()

    return result.get_counts()