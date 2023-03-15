import cirq
from cirq.circuits import InsertStrategy
from cirq_web import BlochSphere

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

simulador = cirq.Simulator()
resultado = simulador.simulate(circuito).final_state_vector

print(circuito)
print(resultado)