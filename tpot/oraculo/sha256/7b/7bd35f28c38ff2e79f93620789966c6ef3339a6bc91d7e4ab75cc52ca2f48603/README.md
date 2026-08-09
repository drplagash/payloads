# 🧬 Payload Analysis

`7bd35f28c38ff2e79f93620789966c6ef3339a6bc91d7e4ab75cc52ca2f48603`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 270 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `methodology` en `hxxps://umai[.]entelijan[.]com/methodology`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7bd35f28c38ff2e79f93620789966c6ef3339a6bc91d7e4ab75cc52ca2f48603`
- **SHA1:** `f535586a4f252e94496f9c51cee7ef0613d74416`
- **MD5:** `f65db2f71ff30942c08ad46ce6b1d0c3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 270 B |
| Entropía | 5.06 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://umai[.]entelijan[.]com/methodology) | strings |
| ip | 190.179.144.XXX | static_analysis |
| hash | 7bd35f28c38ff2e79f93620789966c6ef3339a6bc91d7e4ab75cc52ca2f48603 | static_analysis |
| ip | 185.150.191.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
