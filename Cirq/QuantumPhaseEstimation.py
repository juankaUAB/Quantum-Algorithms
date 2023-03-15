import cirq
from cirq.circuits import InsertStrategy
from cirq_web import BlochSphere

def generate_unitary_qft():
    circuito = cirq.Circuit()
    q0, q1, q2 = [cirq.LineQubit(x) for x in range(0,3)]

    '''transform 101 (5) in computational basis into fourier basis'''
    circuito.append([cirq.X(q0), cirq.X(q2)], strategy=InsertStrategy.NEW_THEN_INLINE)
    circuito.append([cirq.H(q0)], strategy=InsertStrategy.NEW_THEN_INLINE)
    circuito.append([cirq.CZ(q1, q0)**0.5], strategy=InsertStrategy.NEW_THEN_INLINE)
    circuito.append([cirq.CZ(q2, q0)**0.25], strategy=InsertStrategy.NEW_THEN_INLINE)
    circuito.append([cirq.H(q1)], strategy=InsertStrategy.NEW_THEN_INLINE)
    circuito.append([cirq.CZ(q2,q1)**0.5], strategy=InsertStrategy.NEW_THEN_INLINE)
    circuito.append([cirq.H(q2)], strategy=InsertStrategy.NEW_THEN_INLINE)
    
    return cirq.inverse(circuito.unitary)

class MyQFTGate(cirq.Gate):
    def __init__(self):
        super(MyQFTGate, self)

    def _num_qubits_(self):
        return 3

    def _unitary_(self):
        return generate_unitary_qft()

    def _circuit_diagram_info_(self, args):
        return "QFT"

circuito = cirq.Circuit()
q0, q1, q2, q3 = [cirq.LineQubit(x) for x in range(0,4)]

circuito.append([cirq.H(q0), cirq.H(q1), cirq.H(q2), cirq.X(q3)])
circuito.append([cirq.CZ(q0,q3)**0.25])
circuito.append([cirq.CZ(q1,q3)**0.25])
circuito.append([cirq.CZ(q1,q3)**0.25])
circuito.append([cirq.CZ(q2,q3)**0.25])
circuito.append([cirq.CZ(q2,q3)**0.25])
circuito.append([cirq.CZ(q2,q3)**0.25])
circuito.append([cirq.CZ(q2,q3)**0.25])
circuito.append([cirq.qft(q0,q1,q2, without_reverse=True, inverse=True)])
circuito.append([cirq.measure(q0,q1,q2)], strategy=InsertStrategy.NEW)

simulador = cirq.Simulator()
resultado = simulador.run(circuito)

print(circuito)
print(resultado)