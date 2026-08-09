# 🧬 Payload Analysis

`4873879fab2eec88f2d0577ae85f5ffe2fc47526359d6f30b6afce6dfe114b20`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4873879fab2eec88f2d0577ae85f5ffe2fc47526359d6f30b6afce6dfe114b20`
- **SHA1:** `86e96c10992c732e1c4ccf570b931c11b4ac6791`
- **MD5:** `ec4adb78665cc4ac6d6e71827c5428ef`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 117 B |
| Entropía | 5.11 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| hash | 4873879fab2eec88f2d0577ae85f5ffe2fc47526359d6f30b6afce6dfe114b20 | static_analysis |
| ip | 57.151.98.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
