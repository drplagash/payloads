# 🧬 Payload Analysis

`28dde47535e765c23b613d265db7d6afadad14714bca665b2fe2dda7fc9c98e7`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:34+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `28dde47535e765c23b613d265db7d6afadad14714bca665b2fe2dda7fc9c98e7`
- **MD5:** `3971b5677c8bef2ed1b8f69171bb8bca`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 267 B |
| Entropía | 5.03 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.174.XXX | static_analysis |
| url | hxxps://leakix[.]net/, | strings |
| url | hxxps://twitter[.]com/HaboubiAnis) | strings |
| hash | 28dde47535e765c23b613d265db7d6afadad14714bca665b2fe2dda7fc9c98e7 | static_analysis |
| ip | 129.212.220.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
