# 🧬 Payload Analysis

`abe95c78f860c849bdbcb54359c2b37754d404dbc758b794be300a75575571ad`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:49:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `abe95c78f860c849bdbcb54359c2b37754d404dbc758b794be300a75575571ad`
- **SHA1:** `1430e8680586b1adb989b49436f749313cdae33b`
- **MD5:** `3442f96a379d86a57155932d741efe7b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 320 B |
| Entropía | 7.35 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.3; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | abe95c78f860c849bdbcb54359c2b37754d404dbc758b794be300a75575571ad | static_analysis |
| ip | 213.209.159.XXX | artifact_source |

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
