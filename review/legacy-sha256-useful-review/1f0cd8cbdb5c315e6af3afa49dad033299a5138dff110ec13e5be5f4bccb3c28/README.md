# 🧬 Payload Analysis

`1f0cd8cbdb5c315e6af3afa49dad033299a5138dff110ec13e5be5f4bccb3c28`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/1f0cd8cbdb5c315e6af3afa49dad033299a5138dff110ec13e5be5f4bccb3c28.md](../../../../../malware-like/oraculo/botnet/1f0cd8cbdb5c315e6af3afa49dad033299a5138dff110ec13e5be5f4bccb3c28.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1f0cd8cbdb5c315e6af3afa49dad033299a5138dff110ec13e5be5f4bccb3c28`
- **SHA1:** `31fad49554658ab28b581b1e2f5814aafe64f05a`
- **MD5:** `090f3cfbe2e747eed142c3be9b1e8545`

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
| hash | 1f0cd8cbdb5c315e6af3afa49dad033299a5138dff110ec13e5be5f4bccb3c28 | static_analysis |
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
