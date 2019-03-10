from qiskit import IBMQ, QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import execute, Aer
import numpy as np
import matplotlib.pyplot as plt


class HelloQuantum:

    def __init__(self):
        pass
    
    def hello_quantum(self):
        q = QuantumRegister(2)
        c = ClassicalRegister(2)
        qc = QuantumCircuit(q, c)

        qc.h(q[0])
        qc.cx(q[0], q[1])
        qc.measure(q, c)

        backend = Aer.get_backend('qasm_simulator')

        job = execute(qc, backend=backend, shots=1024)
        result = job.result()
        counts = result.get_counts(qc)
        print(qc)
        print(counts)

if __name__ == "__main__":
    hello = HelloQuantum()
    hello.hello_quantum()