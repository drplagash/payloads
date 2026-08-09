# 🧬 Payload Analysis

`541c7350c59b5558395703c7e97e0bdcbe256bb46c7c5543e06eb820584dadca`

## 📌 Resumen

Artefacto identificado como XML 1.0 document, ASCII text, with very long lines (712), with no line terminators de 712 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `adb.sh` en `hxxp://196.251.121.XXX/a3f8d2/adb.sh`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:58:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `541c7350c59b5558395703c7e97e0bdcbe256bb46c7c5543e06eb820584dadca`
- **SHA1:** `a3f78e8f8b9e8d1d4702f450e5ee1f009afbf06e`
- **MD5:** `6474e4addcfb73b560f034d38ea0d72d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (712), with no line terminators |
| Tamaño | 712 B |
| Entropía | 5.22 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (712), with no line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://196.251.121.XXX/a3f8d2/adb.sh; | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| ip | 196.251.121.XXX | static_analysis |
| hash | 541c7350c59b5558395703c7e97e0bdcbe256bb46c7c5543e06eb820584dadca | static_analysis |
| ip | 115.84.178.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
