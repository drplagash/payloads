# 🧬 Payload Analysis

`36a09671bf850b8dec53709b8c1b177599ba0c9dfc77dd810e9e3c4d1d5eab1a`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `36a09671bf850b8dec53709b8c1b177599ba0c9dfc77dd810e9e3c4d1d5eab1a`
- **SHA1:** `6f37fe98eef2850d0b157fb1e175da65f6897342`
- **MD5:** `8b8acb44eabd1dfda4a910b4de6e9ad9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Public Key Version 2 |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Public Key Version 2; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 36a09671bf850b8dec53709b8c1b177599ba0c9dfc77dd810e9e3c4d1d5eab1a | static_analysis |
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
