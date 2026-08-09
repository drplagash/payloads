# 🧬 Payload Analysis

`c549549dc7c0f755d4ba865140b874de3a157294ad8898008962764e4fe70fde`

## 📌 Resumen

Script JavaScript de 1.4 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `gg2` en `hxxp://94.154.43.XXX/gg2`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c549549dc7c0f755d4ba865140b874de3a157294ad8898008962764e4fe70fde`
- **SHA1:** `91af8a8baabd91513397fc9b40ede8626bce7cc6`
- **MD5:** `1d455a5a2aba5e1c02ccc1b402401f00`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (554), with CRLF line terminators |
| Tamaño | 1.4 KiB |
| Entropía | 5.47 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (554), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg2) | strings |
| url | hxxp://94.154.43.XXX/gg2 | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | c549549dc7c0f755d4ba865140b874de3a157294ad8898008962764e4fe70fde | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
