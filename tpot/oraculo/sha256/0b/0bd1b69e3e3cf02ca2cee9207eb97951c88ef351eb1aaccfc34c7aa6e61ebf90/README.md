# 🧬 Payload Analysis

`0bd1b69e3e3cf02ca2cee9207eb97951c88ef351eb1aaccfc34c7aa6e61ebf90`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:43:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0bd1b69e3e3cf02ca2cee9207eb97951c88ef351eb1aaccfc34c7aa6e61ebf90`
- **SHA1:** `bdfcf44445e2339acbd93c93cd6b9b07fdf8a0be`
- **MD5:** `21a5a9134fe7d275897a43e7c737e3de`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Dyalog APL component file 32-bit non-journaled checksummed version -48.-74 |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Dyalog APL component file 32-bit non-journaled checksummed version -48.-74; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0bd1b69e3e3cf02ca2cee9207eb97951c88ef351eb1aaccfc34c7aa6e61ebf90 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
