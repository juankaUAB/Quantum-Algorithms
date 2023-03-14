import cirq
from cirq.circuits import InsertStrategy

circuito = cirq.Circuit()
q0, q1, q2, q3, q4, q5 = [cirq.LineQubit(i) for i in range(0,6)]

circuito.append([cirq.H(q0), cirq.H(q1), cirq.H(q2)])
circuito.append([cirq.CNOT(q0, q3)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append([cirq.CNOT(q1,q4)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append([cirq.CNOT(q2, q5)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append([cirq.CNOT(q1,q4)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append([cirq.CNOT(q1,q5)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append([cirq.H(q0), cirq.H(q1), cirq.H(q2)], strategy=InsertStrategy.NEW_THEN_INLINE)
circuito.append(cirq.measure(q0,q1,q2), strategy=InsertStrategy.NEW)

simulador = cirq.Simulator()
resultado = simulador.run(circuito, repetitions=1000)

histograma = dict()
for e in list(resultado.measurements.values())[0]:
    key = ''.join(str(x) for x in e)
    if key not in histograma:
        histograma[key] = 1
    else:
        histograma[key] += 1


print(circuito)
print(histograma)

'''Now we would have to resolve the equation system to find b'''