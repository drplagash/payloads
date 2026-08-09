# 🧬 Payload Analysis

`c6261eb6637aef67c8f2a7c7cced60818d5a2840072044827d6b5a4f144b58d0`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:08.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c6261eb6637aef67c8f2a7c7cced60818d5a2840072044827d6b5a4f144b58d0`
- **MD5:** `f6d9ef82271b5aa42905caf8d1bb397b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text |
| Tamaño | 444 B |
| Entropía | 5.58 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Mirai-like indicators in strings
Mirai-like indicators in strings

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.167.XXX | static_analysis |
| hash | c6261eb6637aef67c8f2a7c7cced60818d5a2840072044827d6b5a4f144b58d0 | static_analysis |
| ip | 172.110.223.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
