# 🧬 Payload Analysis

`d0b530c7fca8a16b44be886e19dfb4a61a8580b846ed5b77ffc3a861191dcbc3`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d0b530c7fca8a16b44be886e19dfb4a61a8580b846ed5b77ffc3a861191dcbc3`
- **SHA1:** `596f621503891257ab37e0a815da039f39c4e930`
- **MD5:** `7836baebfd6a92ea96043b580fcbf6b4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.07 |
| Strings | 124 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; strings=124; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| url | hxxps://umai[.]enteli | strings |
| url | hxxps://umai[.]entelijan[.]com/methodology) | strings |
| hash | d0b530c7fca8a16b44be886e19dfb4a61a8580b846ed5b77ffc3a861191dcbc3 | static_analysis |
| ip | 209.222.101.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
