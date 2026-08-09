# 🧬 Payload Analysis

`375aa65324ceb90582a59234dae2ebafe64f23d610af6ae50156a016250f9ffe`

## 📌 Resumen

Script JavaScript de 1.2 KiB. La evidencia estática disponible identifica capacidad de descarga remota. Se extrajo como destino remoto `hxxps://return[.]st/`. Se extrajeron 2 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `375aa65324ceb90582a59234dae2ebafe64f23d610af6ae50156a016250f9ffe`
- **MD5:** `33117dbc7edfc8a93141ef23e7e9efd4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (906), with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.64 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (906), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://return[.]st/?ref=Q7hw1uZ6pEz8LTEX | strings |
| url | hxxp://ip/x86; | strings |
| url | hxxps://return[.]st/?ref=Q7hw1uZ6pEz8LTEX;307; | strings |
| hash | 375aa65324ceb90582a59234dae2ebafe64f23d610af6ae50156a016250f9ffe | static_analysis |
| ip | 31.59.160.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
