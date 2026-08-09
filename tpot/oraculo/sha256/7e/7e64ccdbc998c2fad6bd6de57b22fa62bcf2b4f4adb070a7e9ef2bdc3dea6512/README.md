# 🧬 Payload Analysis

`7e64ccdbc998c2fad6bd6de57b22fa62bcf2b4f4adb070a7e9ef2bdc3dea6512`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:48:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7e64ccdbc998c2fad6bd6de57b22fa62bcf2b4f4adb070a7e9ef2bdc3dea6512`
- **SHA1:** `7925b91d7a57339430b644cbe14a8c116199b07a`
- **MD5:** `28dda57bf39a4f9ada3ca689d6d55379`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 118 B |
| Entropía | 5.07 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.144.XXX | static_analysis |
| hash | 7e64ccdbc998c2fad6bd6de57b22fa62bcf2b4f4adb070a7e9ef2bdc3dea6512 | static_analysis |
| ip | 20.150.193.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
