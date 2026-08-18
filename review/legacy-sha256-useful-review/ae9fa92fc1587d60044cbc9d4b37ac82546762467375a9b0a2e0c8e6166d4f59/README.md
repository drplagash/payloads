# 🧬 Payload Analysis

`ae9fa92fc1587d60044cbc9d4b37ac82546762467375a9b0a2e0c8e6166d4f59`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/ae9fa92fc1587d60044cbc9d4b37ac82546762467375a9b0a2e0c8e6166d4f59.md](../../../../../malware-like/oraculo/botnet/ae9fa92fc1587d60044cbc9d4b37ac82546762467375a9b0a2e0c8e6166d4f59.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ae9fa92fc1587d60044cbc9d4b37ac82546762467375a9b0a2e0c8e6166d4f59`
- **SHA1:** `cad59b9e48100c4c4019809bdb07d03823315b83`
- **MD5:** `3bc2b3fe25502b9da4763283cd820175`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | ae9fa92fc1587d60044cbc9d4b37ac82546762467375a9b0a2e0c8e6166d4f59 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
