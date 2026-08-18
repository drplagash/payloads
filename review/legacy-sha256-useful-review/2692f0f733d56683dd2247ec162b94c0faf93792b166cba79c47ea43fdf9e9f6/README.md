# 🧬 Payload Analysis

`2692f0f733d56683dd2247ec162b94c0faf93792b166cba79c47ea43fdf9e9f6`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/2692f0f733d56683dd2247ec162b94c0faf93792b166cba79c47ea43fdf9e9f6.md](../../../../../malware-like/oraculo/botnet/2692f0f733d56683dd2247ec162b94c0faf93792b166cba79c47ea43fdf9e9f6.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:32:58.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2692f0f733d56683dd2247ec162b94c0faf93792b166cba79c47ea43fdf9e9f6`
- **SHA1:** `263a123d309751f83bb1f0029154a028453cd9ff`
- **MD5:** `bd211b45d10bec4a686f063d4d5c5dec`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 2692f0f733d56683dd2247ec162b94c0faf93792b166cba79c47ea43fdf9e9f6 | static_analysis |
| ip | 101.50.75.XXX | artifact_source |

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
