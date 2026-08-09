# 🧬 Payload Analysis

`b5288cfe53e8a4346d36bb8baee1408d69ee0bf14ea0f0b8afd26494506ea558`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:01:51+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b5288cfe53e8a4346d36bb8baee1408d69ee0bf14ea0f0b8afd26494506ea558`
- **SHA1:** `32ccada9421ca86c3009da46c0674f4287bcc558`
- **MD5:** `badc0eb0b7abc4c63267b42b3bf4083f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 49 B |
| Entropía | 4.53 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | b5288cfe53e8a4346d36bb8baee1408d69ee0bf14ea0f0b8afd26494506ea558 | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
