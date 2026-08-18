# 🧬 Payload Analysis

`b4714efad05b3bd72cd3e9fd3b8a1227a7d25072d86f465a13b3cbf01cbec3e8`

## 📌 Resumen

Artefacto de 1.4 KiB. Presenta entropía elevada (7.85), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b4714efad05b3bd72cd3e9fd3b8a1227a7d25072d86f465a13b3cbf01cbec3e8`
- **MD5:** `61c620ab123c13a19cebd43042923c4c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.85 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Alta entropía / posible empaquetado o cifrado**

## 🔬 Evidencia de clasificación

- High entropy (7.8) — posible packer/encrypted
High entropy (7.8) — posible packer/encrypted

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | b4714efad05b3bd72cd3e9fd3b8a1227a7d25072d86f465a13b3cbf01cbec3e8 | static_analysis |
| ip | 185.125.190.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
