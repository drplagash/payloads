# 🧬 Payload Analysis

`57fcb6dbb64bba4446af9a011aa49e4c31400887d80cc54fe255071c28f226a3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:02:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `57fcb6dbb64bba4446af9a011aa49e4c31400887d80cc54fe255071c28f226a3`
- **SHA1:** `b99f2dec1fadc514e0d56d49245253acdb7c2fca`
- **MD5:** `7af04e98b36f1aa7f6a03e2518a96714`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 57fcb6dbb64bba4446af9a011aa49e4c31400887d80cc54fe255071c28f226a3 | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

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
