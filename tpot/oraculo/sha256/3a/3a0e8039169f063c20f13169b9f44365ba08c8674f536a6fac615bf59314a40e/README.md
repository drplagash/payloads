# 🧬 Payload Analysis

`3a0e8039169f063c20f13169b9f44365ba08c8674f536a6fac615bf59314a40e`

## 📌 Resumen

Script JavaScript de 1.3 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `gg2` en `hxxp://2.26.124.XXX/gg2`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3a0e8039169f063c20f13169b9f44365ba08c8674f536a6fac615bf59314a40e`
- **SHA1:** `b2ff722a293c69831e88e3c70e65651b09975cb9`
- **MD5:** `50b6f111b9d41c8d592bbb5487c4f305`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (696), with CRLF line terminators |
| Tamaño | 1.3 KiB |
| Entropía | 5.35 |
| Strings | 15 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Comunicación remota**
3. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (696), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://2.26.124.XXX/gg2 | strings |
| url | hxxp://2.26.124.XXX/gg2) | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 2.26.124.XXX | static_analysis |
| hash | 3a0e8039169f063c20f13169b9f44365ba08c8674f536a6fac615bf59314a40e | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
