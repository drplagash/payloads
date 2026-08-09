# 🧬 Payload Analysis

`09c98cec096d94909d4a5be672075e76dd66b7d502cc855719311d2dabcb5bb7`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:44:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `09c98cec096d94909d4a5be672075e76dd66b7d502cc855719311d2dabcb5bb7`
- **SHA1:** `de88eae90c5ded34f03863c27c75fdc34c798c04`
- **MD5:** `7748eeb0511b01656ce63f5d0296d99b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 262 B |
| Entropía | 5.09 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| url | hxxps://umai[.]entelijan[.]com/methodology) | strings |
| hash | 09c98cec096d94909d4a5be672075e76dd66b7d502cc855719311d2dabcb5bb7 | static_analysis |
| ip | 104.243.43.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
