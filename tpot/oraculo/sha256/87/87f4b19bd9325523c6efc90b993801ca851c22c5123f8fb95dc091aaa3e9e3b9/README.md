# 🧬 Payload Analysis

`87f4b19bd9325523c6efc90b993801ca851c22c5123f8fb95dc091aaa3e9e3b9`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:13:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `87f4b19bd9325523c6efc90b993801ca851c22c5123f8fb95dc091aaa3e9e3b9`
- **SHA1:** `871184c57714aadb190e1a93a287b00f8d464a29`
- **MD5:** `6042d3ccf56b1ae392d332ef2fa5b4b5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Sony PlayStation Audio |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Sony PlayStation Audio; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 87f4b19bd9325523c6efc90b993801ca851c22c5123f8fb95dc091aaa3e9e3b9 | static_analysis |
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
