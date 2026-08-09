# 🧬 Payload Analysis

`3d6bfa56dea2d45684ecb744722a0ef9dba1c5cd0c30c9cd97ae9f3ffbacf342`

## 📌 Resumen

Artefacto de 1.4 KiB. Entropía registrada: 7.03. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3d6bfa56dea2d45684ecb744722a0ef9dba1c5cd0c30c9cd97ae9f3ffbacf342`
- **MD5:** `aa3ec70166c6521df41cbabbe362f10f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.03 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Alta entropía / posible empaquetado o cifrado**

## 🔬 Evidencia de clasificación

- High entropy (7.0) — posible packer/encrypted
High entropy (7.0) — posible packer/encrypted

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 3d6bfa56dea2d45684ecb744722a0ef9dba1c5cd0c30c9cd97ae9f3ffbacf342 | static_analysis |
| ip | 95.158.29.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
