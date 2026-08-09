# 🧬 Payload Analysis

`b01ff3e72790c15863843685eb447b1de85f5214d69b3e26c08c80821405f794`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (624), with CRLF line terminators de 803 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `envelope` en `hxxp://schemas[.]xmlsoap[.]org/soap/envelope/`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b01ff3e72790c15863843685eb447b1de85f5214d69b3e26c08c80821405f794`
- **SHA1:** `12637223ea24793317b408027e86256e2596e4d2`
- **MD5:** `d99cef49d62c6fde72884a566136521d`

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
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://139.135.59.XXX:36773/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| ip | 139.135.59.XXX | static_analysis |
| hash | b01ff3e72790c15863843685eb447b1de85f5214d69b3e26c08c80821405f794 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
