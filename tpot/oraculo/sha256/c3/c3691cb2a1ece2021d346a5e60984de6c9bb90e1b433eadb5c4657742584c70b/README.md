# 🧬 Payload Analysis

`c3691cb2a1ece2021d346a5e60984de6c9bb90e1b433eadb5c4657742584c70b`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:02:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c3691cb2a1ece2021d346a5e60984de6c9bb90e1b433eadb5c4657742584c70b`
- **SHA1:** `7352e0a3975b6d6818210b37057bf46711211604`
- **MD5:** `b893bd1505d7b33ca2da61f6092bd8f6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Dyalog APL version 86.-127 |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Dyalog APL version 86.-127; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c3691cb2a1ece2021d346a5e60984de6c9bb90e1b433eadb5c4657742584c70b | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

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
