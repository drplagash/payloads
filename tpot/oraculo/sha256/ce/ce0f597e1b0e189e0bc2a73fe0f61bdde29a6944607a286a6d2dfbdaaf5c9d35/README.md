# 🧬 Payload Analysis

`ce0f597e1b0e189e0bc2a73fe0f61bdde29a6944607a286a6d2dfbdaaf5c9d35`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (620), with CRLF line terminators de 799 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m` en `hxxp://[internal-ip-redacted]:8088/Mozi.m`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ce0f597e1b0e189e0bc2a73fe0f61bdde29a6944607a286a6d2dfbdaaf5c9d35`
- **SHA1:** `657f58f34f2dc533a809b72d93100b5c6383b2c1`
- **MD5:** `14b1d63c32a6feb4322a8b53a99b04ef`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (620), with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.47 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (620), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]:8088/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | ce0f597e1b0e189e0bc2a73fe0f61bdde29a6944607a286a6d2dfbdaaf5c9d35 | static_analysis |
| ip | 202.141.94.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
