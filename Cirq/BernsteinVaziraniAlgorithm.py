import cirq
from cirq.circuits import InsertStrategy

circuito = cirq.Circuit()
q0, q1, q2, q3 = [cirq.LineQubit(i) for i in range(0,4)]

circuito.append([cirq.H(q0), cirq.H(q1), cirq.H(q2)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append([cirq.X(q3), cirq.H(q3)])
circuito.append([cirq.I(q0), cirq.I(q2)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append([cirq.CNOT(q1,q3)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append([cirq.H(q0), cirq.H(q1), cirq.H(q2)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append(cirq.measure(q0,q1,q2), strategy=InsertStrategy.NEW)

simulador = cirq.Simulator()
resultado = simulador.run(circuito)

print(circuito)
print(resultado)