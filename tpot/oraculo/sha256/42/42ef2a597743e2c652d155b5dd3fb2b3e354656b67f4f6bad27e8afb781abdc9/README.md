# 🧬 Payload Analysis

`42ef2a597743e2c652d155b5dd3fb2b3e354656b67f4f6bad27e8afb781abdc9`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 195 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `genomecrawler` en `hxxps://www[.]nokia[.]com/genomecrawler`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:03.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `42ef2a597743e2c652d155b5dd3fb2b3e354656b67f4f6bad27e8afb781abdc9`
- **SHA1:** `53e7242df34344411fcc5144e5ebcaf1c3af9113`
- **MD5:** `a3123d21df57662f4157a30f7583fd6d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 195 B |
| Entropía | 5.21 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://www[.]nokia[.]com/genomecrawler) | strings |
| ip | 190.179.168.XXX | static_analysis |
| hash | 42ef2a597743e2c652d155b5dd3fb2b3e354656b67f4f6bad27e8afb781abdc9 | static_analysis |
| ip | 216.180.246.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
