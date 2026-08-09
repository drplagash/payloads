# 🧬 Payload Analysis

`c3c2805cc64731c3a7db991c8ab7a992f84d6951228602006b7e469297d32a21`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:08:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c3c2805cc64731c3a7db991c8ab7a992f84d6951228602006b7e469297d32a21`
- **SHA1:** `52e7d0a3a7058a14684b6019c1e28a2939cc52f4`
- **MD5:** `fc46eaa7b58bceb43dc2e1384cb15e84`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | zlib compressed data |
| Tamaño | 1.4 KiB |
| Entropía | 7.85 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=zlib compressed data; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c3c2805cc64731c3a7db991c8ab7a992f84d6951228602006b7e469297d32a21 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
