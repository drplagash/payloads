# 🧬 Payload Analysis

`a3151a72f292e3257088a6a34cf951ac744d1c6270ac2480b3441fd8bff1a6ab`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:11:29+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a3151a72f292e3257088a6a34cf951ac744d1c6270ac2480b3441fd8bff1a6ab`
- **SHA1:** `657967b3d5b4a36d7ea954c5df3c1ebf7a2b5a90`
- **MD5:** `8c471c996f4555f497e2fe28a79a0878`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Dyalog APL version -109.-78 |
| Tamaño | 1.4 KiB |
| Entropía | 7.83 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Dyalog APL version -109.-78; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | a3151a72f292e3257088a6a34cf951ac744d1c6270ac2480b3441fd8bff1a6ab | static_analysis |
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
