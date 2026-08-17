# Payload repository audit

Auditoria inicial de tpot/oraculo/sha256.

Resultado:
- weak-sha256-noise.txt: entradas debiles o ruido.
- useful-sha256-review.txt: entradas con posible valor operativo.
- unknown-sha256-review.txt: entradas dudosas para revision manual.

Politica:
No se borra nada directo de main.
Primero se clasifica, luego se migra en tandas revisables.
