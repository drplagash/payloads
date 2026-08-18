# 🧬 Payload Analysis

`54fe619a722a67ed6c15bef90b6a9b4e507a65aa89ed1cd8f67b3773e477cfbc`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/54fe619a722a67ed6c15bef90b6a9b4e507a65aa89ed1cd8f67b3773e477cfbc.md](../../../../../malware-like/oraculo/botnet/54fe619a722a67ed6c15bef90b6a9b4e507a65aa89ed1cd8f67b3773e477cfbc.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:35:39.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `54fe619a722a67ed6c15bef90b6a9b4e507a65aa89ed1cd8f67b3773e477cfbc`
- **SHA1:** `b2d8d75fe295db753bdbe926f41a072ba84bcc2f`
- **MD5:** `461324ddaa8c7d2bc9dec6fe4f8105b5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 54fe619a722a67ed6c15bef90b6a9b4e507a65aa89ed1cd8f67b3773e477cfbc | static_analysis |
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
