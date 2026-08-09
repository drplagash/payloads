# 🧬 Payload Analysis

`9f9919f2e3b1fcba472b39f2d94b7727f9f0ab862adb9a11c5c4ad47cb54bcc8`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9f9919f2e3b1fcba472b39f2d94b7727f9f0ab862adb9a11c5c4ad47cb54bcc8`
- **SHA1:** `cbbf8366c54abcd172e719650e9d177cfcbe5ab7`
- **MD5:** `e11cee992b482a642aa0e5e62634e999`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 173 B |
| Entropía | 5.24 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| hash | 9f9919f2e3b1fcba472b39f2d94b7727f9f0ab862adb9a11c5c4ad47cb54bcc8 | static_analysis |
| ip | 45.95.147.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
