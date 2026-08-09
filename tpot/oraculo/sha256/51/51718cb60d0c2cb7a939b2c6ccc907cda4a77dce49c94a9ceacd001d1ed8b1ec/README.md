# 🧬 Payload Analysis

`51718cb60d0c2cb7a939b2c6ccc907cda4a77dce49c94a9ceacd001d1ed8b1ec`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `51718cb60d0c2cb7a939b2c6ccc907cda4a77dce49c94a9ceacd001d1ed8b1ec`
- **SHA1:** `ff216eb0734bcf5d1e764613f43746a0d649184f`
- **MD5:** `61c3c20e89ead66a524268807d7ebfb3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 90 B |
| Entropía | 4.91 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 239.255.255.XXX | static_analysis |
| hash | 51718cb60d0c2cb7a939b2c6ccc907cda4a77dce49c94a9ceacd001d1ed8b1ec | static_analysis |
| ip | 45.205.1.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
