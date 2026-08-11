# 🧬 Payload Analysis

`1523d58dd40ff190ca546ab5e3bd885ac8f390314541e7b9e9398dd13c8f339c`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/1523d58dd40ff190ca546ab5e3bd885ac8f390314541e7b9e9398dd13c8f339c.md](../../../../../malware-like/oraculo/botnet/1523d58dd40ff190ca546ab5e3bd885ac8f390314541e7b9e9398dd13c8f339c.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:13.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1523d58dd40ff190ca546ab5e3bd885ac8f390314541e7b9e9398dd13c8f339c`
- **MD5:** `d12bed8802b2afc02d63ee334a495f89`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 500 B |
| Entropía | 5.37 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Mirai-like indicators in strings
Mirai-like indicators in strings

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 1523d58dd40ff190ca546ab5e3bd885ac8f390314541e7b9e9398dd13c8f339c | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers3 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
