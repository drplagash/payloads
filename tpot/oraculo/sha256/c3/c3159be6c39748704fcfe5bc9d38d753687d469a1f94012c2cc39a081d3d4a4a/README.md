# 🧬 Payload Analysis

`c3159be6c39748704fcfe5bc9d38d753687d469a1f94012c2cc39a081d3d4a4a`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 260 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `methodology` en `hxxps://umai[.]entelijan[.]com/methodology`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c3159be6c39748704fcfe5bc9d38d753687d469a1f94012c2cc39a081d3d4a4a`
- **SHA1:** `8c74d5838fd30d76c82089f78b5ddd8caa865287`
- **MD5:** `90bd0a4f0b7a31b16365709131b74768`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 260 B |
| Entropía | 5.07 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://umai[.]entelijan[.]com/methodology) | strings |
| ip | 190.179.144.XXX | static_analysis |
| hash | c3159be6c39748704fcfe5bc9d38d753687d469a1f94012c2cc39a081d3d4a4a | static_analysis |
| ip | 185.150.191.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
