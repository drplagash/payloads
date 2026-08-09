# 🧬 Payload Analysis

`2c5b930ef1b49cb67e69d8966d64c8656981ac64cc374695ed6fe4b1c258a16e`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 4.0 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `methodology` en `hxxps://umai[.]entelijan[.]com/methodology`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2c5b930ef1b49cb67e69d8966d64c8656981ac64cc374695ed6fe4b1c258a16e`
- **SHA1:** `13de578062cbbae5a00b9c7eeb9637c909117f71`
- **MD5:** `dc9840262d76436c36f7eda6c1d4d24a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.06 |
| Strings | 125 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; strings=125; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://umai[.]entelijan[.]com/methodology) | strings |
| ip | 190.179.168.XXX | static_analysis |
| hash | 2c5b930ef1b49cb67e69d8966d64c8656981ac64cc374695ed6fe4b1c258a16e | static_analysis |
| ip | 209.222.101.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
