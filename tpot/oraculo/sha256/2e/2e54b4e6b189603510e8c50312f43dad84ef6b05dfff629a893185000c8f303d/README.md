# 🧬 Payload Analysis

`2e54b4e6b189603510e8c50312f43dad84ef6b05dfff629a893185000c8f303d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2e54b4e6b189603510e8c50312f43dad84ef6b05dfff629a893185000c8f303d`
- **SHA1:** `a040223620502da39cfd406a8c0d1b3d9331e9b2`
- **MD5:** `ca2926052509328f61fd43f80ebc2ea5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 864 B |
| Entropía | 5.56 |
| Strings | 24 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| ip | 216.126.224.XXX | static_analysis |
| hash | 2e54b4e6b189603510e8c50312f43dad84ef6b05dfff629a893185000c8f303d | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
