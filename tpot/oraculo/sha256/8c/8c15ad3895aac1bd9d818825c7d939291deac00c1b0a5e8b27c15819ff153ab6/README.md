# 🧬 Payload Analysis

`8c15ad3895aac1bd9d818825c7d939291deac00c1b0a5e8b27c15819ff153ab6`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/8c15ad3895aac1bd9d818825c7d939291deac00c1b0a5e8b27c15819ff153ab6.md](../../../../../malware-like/oraculo/botnet/8c15ad3895aac1bd9d818825c7d939291deac00c1b0a5e8b27c15819ff153ab6.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8c15ad3895aac1bd9d818825c7d939291deac00c1b0a5e8b27c15819ff153ab6`
- **SHA1:** `a6c8c84336ed77404d8bb0a14dc6920991f15f88`
- **MD5:** `1d168f65585531b2e5c02aae79a67579`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 8c15ad3895aac1bd9d818825c7d939291deac00c1b0a5e8b27c15819ff153ab6 | static_analysis |
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
