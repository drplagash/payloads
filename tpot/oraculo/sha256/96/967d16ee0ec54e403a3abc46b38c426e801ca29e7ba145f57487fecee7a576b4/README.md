# 🧬 Payload Analysis

`967d16ee0ec54e403a3abc46b38c426e801ca29e7ba145f57487fecee7a576b4`

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

- **SHA256:** `967d16ee0ec54e403a3abc46b38c426e801ca29e7ba145f57487fecee7a576b4`
- **SHA1:** `89246ff4c93add193e80d7e0eec17505e3f5c1f2`
- **MD5:** `d4c3f3a3b00087be121d024532a3d7fd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | 370 XA sysV pure executable not stripped - version 20664 - 5.2 format |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=370 XA sysV pure executable not stripped - version 20664 - 5.2 format; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 967d16ee0ec54e403a3abc46b38c426e801ca29e7ba145f57487fecee7a576b4 | static_analysis |
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
