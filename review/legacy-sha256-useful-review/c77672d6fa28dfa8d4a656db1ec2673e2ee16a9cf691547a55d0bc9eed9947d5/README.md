# 🧬 Payload Analysis

`c77672d6fa28dfa8d4a656db1ec2673e2ee16a9cf691547a55d0bc9eed9947d5`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como DOS executable (COM), start instruction 0x8c29292d c8ffb15f. Presenta entropía elevada (7.86), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c77672d6fa28dfa8d4a656db1ec2673e2ee16a9cf691547a55d0bc9eed9947d5`
- **MD5:** `e050bb9ac375adb001233cc5745e556b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0x8c29292d c8ffb15f |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0x8c29292d c8ffb15f; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c77672d6fa28dfa8d4a656db1ec2673e2ee16a9cf691547a55d0bc9eed9947d5 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
