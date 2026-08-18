# Hallazgos

Resumen humano del volumen procesado por Oraculo SOC desde telemetría T-Pot.

Esta carpeta existe para mostrar escala sin convertir el repositorio en un basural de hashes.

## Resumen

| Capa | Cantidad | Qué significa |
|---|---:|---|
| Registros históricos procesados | 40000+ | Material crudo heredado del flujo inicial de T-Pot/publisher |
| Review útil legacy | 24739 | Entradas que conservaron señales suficientes para revisión posterior |
| High-signal T-Pot | 517 | Artefactos con comandos, IOCs, metadata y/o detecciones útiles |
| Campañas publicadas | 1 | Caso humano agrupado y explicado |
| Firmas confirmadas completas | 1 | Payload con carpeta completa de análisis, evidencia, metadata, raw inerte y YARA |

## Lectura correcta

No todo registro crudo es malware.

No todo hash es un caso.

No todo payload HTTP es un binario.

El trabajo de Oraculo SOC es separar ruido de señal, agrupar campañas, promover firmas útiles y convertir telemetría de honeypot en evidencia defensiva.

## Entradas principales

- [`high-signal-517.md`](high-signal-517.md)
- [`useful-review-24739.md`](useful-review-24739.md)
- [`legacy-40000.md`](legacy-40000.md)
