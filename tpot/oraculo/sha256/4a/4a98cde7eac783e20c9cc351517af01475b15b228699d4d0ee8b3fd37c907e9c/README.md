# 🧬 Payload Analysis

`4a98cde7eac783e20c9cc351517af01475b15b228699d4d0ee8b3fd37c907e9c`

## 📌 Resumen

Script JavaScript de 1.4 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `gg` en `hxxp://2.26.124.XXX:99/gg`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4a98cde7eac783e20c9cc351517af01475b15b228699d4d0ee8b3fd37c907e9c`
- **SHA1:** `1ff3390a5582c3a08b81ed3290258c0fd3b57484`
- **MD5:** `55af5ed52f583456c37aa57254b26efc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (555), with CRLF line terminators |
| Tamaño | 1.4 KiB |
| Entropía | 5.45 |
| Strings | 23 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Comunicación remota**
3. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (555), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://2.26.124.XXX:99/gg) | strings |
| url | hxxp://2.26.124.XXX:99/gg | strings |
| ip | 2.26.124.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | 4a98cde7eac783e20c9cc351517af01475b15b228699d4d0ee8b3fd37c907e9c | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
