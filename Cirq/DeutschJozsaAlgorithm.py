import cirq
from cirq.circuits import InsertStrategy

circuito = cirq.Circuit()
q0, q1, q2, q3 = [cirq.LineQubit(i) for i in range(0,4)]

circuito.append([cirq.H(q0), cirq.H(q1), cirq.H(q2), cirq.X(q3)])
circuito.append([cirq.X(q0), cirq.X(q2), cirq.H(q3)])
circuito.append([cirq.CNOT(q0, q3), cirq.CNOT(q1, q3), cirq.CNOT(q2, q3)])
circuito.append([cirq.X(q0), cirq.H(q1), cirq.X(q2)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append([cirq.H(q0), cirq.H(q2)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append(cirq.measure(q0,q1,q2))

simulador = cirq.Simulator()
resultado = simulador.run(circuito)

print(circuito)
print(resultado)