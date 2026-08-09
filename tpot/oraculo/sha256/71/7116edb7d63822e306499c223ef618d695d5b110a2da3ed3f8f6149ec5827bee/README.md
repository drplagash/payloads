# 🧬 Payload Analysis

`7116edb7d63822e306499c223ef618d695d5b110a2da3ed3f8f6149ec5827bee`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (624), with CRLF line terminators de 803 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `encoding` en `hxxp://schemas[.]xmlsoap[.]org/soap/encoding/`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:28:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7116edb7d63822e306499c223ef618d695d5b110a2da3ed3f8f6149ec5827bee`
- **SHA1:** `ccfd46e296e734d39d137821ab7a9c873c5c12ff`
- **MD5:** `1b889d6d88a5fa08f38327be45355e78`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (624), with CRLF line terminators |
| Tamaño | 803 B |
| Entropía | 5.47 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (624), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://203.101.186.XXX:41588/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| ip | 203.101.186.XXX | static_analysis |
| hash | 7116edb7d63822e306499c223ef618d695d5b110a2da3ed3f8f6149ec5827bee | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
