# 🧬 Payload Analysis

`c82529d6707e5328bfd51afd12ac2a0a972bed0c817034007c38cdea1d97936a`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:25:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c82529d6707e5328bfd51afd12ac2a0a972bed0c817034007c38cdea1d97936a`
- **SHA1:** `7c665d54fa7607befd526c9da33856d9d4814aa6`
- **MD5:** `6a7e236a888c6804ce093da63294ff43`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Excel 3 BIFF 3 |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Excel 3 BIFF 3; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c82529d6707e5328bfd51afd12ac2a0a972bed0c817034007c38cdea1d97936a | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

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
