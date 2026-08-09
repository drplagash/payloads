# 🧬 Payload Analysis

`6d85c1e10ee020fce0daf741fff722cd1afac6a66821062cdcb8e19ad8dd2354`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (677), with CRLF line terminators de 1.3 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `cumshotnews` en `hxxp://192.142.28.XXX/cumshotnews`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6d85c1e10ee020fce0daf741fff722cd1afac6a66821062cdcb8e19ad8dd2354`
- **SHA1:** `4e1725cf588a96935215d02cbc6898aec72dfcfb`
- **MD5:** `10bb43ee73568d5ecbb008cb31384973`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (677), with CRLF line terminators |
| Tamaño | 1.3 KiB |
| Entropía | 5.66 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (677), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://192.142.28.XXX/cumshotnews; | strings |
| ip | 192.142.28.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | 6d85c1e10ee020fce0daf741fff722cd1afac6a66821062cdcb8e19ad8dd2354 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
