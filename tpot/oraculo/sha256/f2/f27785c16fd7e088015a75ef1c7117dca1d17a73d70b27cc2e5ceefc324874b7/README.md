# 🧬 Payload Analysis

`f27785c16fd7e088015a75ef1c7117dca1d17a73d70b27cc2e5ceefc324874b7`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 214 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `index2.asp` en `hxxp://190.179.177.XXX:443/cgi-bin/index2.asp`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f27785c16fd7e088015a75ef1c7117dca1d17a73d70b27cc2e5ceefc324874b7`
- **SHA1:** `5f08d631d3fcde55e273fe93cd61df5e63c90179`
- **MD5:** `3f1de385d817ea535497d0a208c1d089`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 214 B |
| Entropía | 5.39 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://190.179.177.XXX:443/cgi-bin/index2.asp | strings |
| ip | 190.179.177.XXX | static_analysis |
| ip | 126.0.0.XXX | static_analysis |
| hash | f27785c16fd7e088015a75ef1c7117dca1d17a73d70b27cc2e5ceefc324874b7 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
