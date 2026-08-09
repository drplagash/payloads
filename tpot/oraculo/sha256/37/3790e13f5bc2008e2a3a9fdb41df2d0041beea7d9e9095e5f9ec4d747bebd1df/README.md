# 🧬 Payload Analysis

`3790e13f5bc2008e2a3a9fdb41df2d0041beea7d9e9095e5f9ec4d747bebd1df`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3790e13f5bc2008e2a3a9fdb41df2d0041beea7d9e9095e5f9ec4d747bebd1df`
- **SHA1:** `3a0f66bdc31a56b425d0937bf7fa6687775878f4`
- **MD5:** `9d4521670f7595b7d8556a78645dccf4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | MPEG ADTS, layer III, v1, 160 kbps, Stereo |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=MPEG ADTS, layer III, v1, 160 kbps, Stereo; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 3790e13f5bc2008e2a3a9fdb41df2d0041beea7d9e9095e5f9ec4d747bebd1df | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | media or resource |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
