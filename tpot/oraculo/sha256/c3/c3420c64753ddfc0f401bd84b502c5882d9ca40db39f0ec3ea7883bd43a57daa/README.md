# 🧬 Payload Analysis

`c3420c64753ddfc0f401bd84b502c5882d9ca40db39f0ec3ea7883bd43a57daa`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.12. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:49.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c3420c64753ddfc0f401bd84b502c5882d9ca40db39f0ec3ea7883bd43a57daa`
- **MD5:** `dcb32031a0a7bf7c2fd30e32dc4136be`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.12 |
| Strings | 13 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.1; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c3420c64753ddfc0f401bd84b502c5882d9ca40db39f0ec3ea7883bd43a57daa | static_analysis |
| ip | 213.157.51.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
