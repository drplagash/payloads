# 🧬 Payload Analysis

`4109dc6ceec640fc908db0bce960135838d0b849b901035df1d3dd0cbe97c0cc`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:06:31+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4109dc6ceec640fc908db0bce960135838d0b849b901035df1d3dd0cbe97c0cc`
- **SHA1:** `8e67e68a8ee5b76aed876edefc4c4ff83ad000a6`
- **MD5:** `ba2b92dee5c8b4eafa939ef3d3d7bbd5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.74 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/1999/xlink | strings |
| url | hxxp://www[.]w3[.]org/2000/svg | strings |
| hash | 4109dc6ceec640fc908db0bce960135838d0b849b901035df1d3dd0cbe97c0cc | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
