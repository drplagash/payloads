# 🧬 Payload Analysis

`a80a93996810f64c5feacccdd231dabcd6e72e7205da4e37ac5d9e8ea10fc893`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (480), with CRLF line terminators de 793 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `x86` en `hxxp://217.60.195.XXX:8080/x86`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:41:09.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a80a93996810f64c5feacccdd231dabcd6e72e7205da4e37ac5d9e8ea10fc893`
- **SHA1:** `cf0b7bee72b04e31fa3dc9496f852bb30fc3d6c5`
- **MD5:** `256e7cdc07438b7dab1befbb906069aa`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (480), with CRLF line terminators |
| Tamaño | 793 B |
| Entropía | 5.65 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (480), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://217.60.195.XXX:8080/x86; | strings |
| ip | 217.60.195.XXX | static_analysis |
| hash | a80a93996810f64c5feacccdd231dabcd6e72e7205da4e37ac5d9e8ea10fc893 | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
