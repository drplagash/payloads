# 🧬 Payload Analysis

`2bd81a6c71cc2882c7e58fbf1ee240cc62eb511eefedb264a7521f4e83888666`

## 📌 Resumen

Artefacto de 4.0 KiB. Presenta entropía elevada (7.35), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2bd81a6c71cc2882c7e58fbf1ee240cc62eb511eefedb264a7521f4e83888666`
- **MD5:** `50873ef5c82a304b1fe94b7fd2743893`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.35 |
| Strings | 18 |

## 🧠 Comportamiento observado

1. **Alta entropía / posible empaquetado o cifrado**

## 🔬 Evidencia de clasificación

- High entropy (7.3) — posible packer/encrypted
High entropy (7.3) — posible packer/encrypted

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 2bd81a6c71cc2882c7e58fbf1ee240cc62eb511eefedb264a7521f4e83888666 | static_analysis |
| ip | 95.158.29.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
