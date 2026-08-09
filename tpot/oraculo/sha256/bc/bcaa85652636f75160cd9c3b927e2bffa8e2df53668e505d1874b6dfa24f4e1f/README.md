# 🧬 Payload Analysis

`bcaa85652636f75160cd9c3b927e2bffa8e2df53668e505d1874b6dfa24f4e1f`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bcaa85652636f75160cd9c3b927e2bffa8e2df53668e505d1874b6dfa24f4e1f`
- **SHA1:** `0215e582cf3f8833451d3d748e528fbde3c077ea`
- **MD5:** `fa42400c8af523dcf074f90c6174fd87`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 266 B |
| Entropía | 5.08 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.144.XXX | static_analysis |
| url | hxxps://umai[.]entelijan[.]com/methodology) | strings |
| hash | bcaa85652636f75160cd9c3b927e2bffa8e2df53668e505d1874b6dfa24f4e1f | static_analysis |
| ip | 185.150.191.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
