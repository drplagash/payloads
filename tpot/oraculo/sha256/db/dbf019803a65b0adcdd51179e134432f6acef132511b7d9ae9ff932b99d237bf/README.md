# 🧬 Payload Analysis

`dbf019803a65b0adcdd51179e134432f6acef132511b7d9ae9ff932b99d237bf`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (622), with CRLF line terminators de 801 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `encoding` en `hxxp://schemas[.]xmlsoap[.]org/soap/encoding/`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dbf019803a65b0adcdd51179e134432f6acef132511b7d9ae9ff932b99d237bf`
- **SHA1:** `e7e69318244ad75696c7cf7f18a7a25a4d52542b`
- **MD5:** `1b6331dcc99f1f8f666b11eb80b433bb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (622), with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.46 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (622), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://72.255.3.XXX:37070/Mozi.m | strings |
| ip | 72.255.3.XXX | static_analysis |
| hash | dbf019803a65b0adcdd51179e134432f6acef132511b7d9ae9ff932b99d237bf | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
