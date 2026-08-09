# 🧬 Payload Analysis

`e4c2946a099d3922c054bccac03ffffbe33b934bcaba85df4c8b789a08c81252`

## 📌 Resumen

Artefacto identificado como XML 1.0 document, ASCII text, with very long lines (624), with no line terminators de 624 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m` en `hxxp://103.213.112.XXX:58691/Mozi.m`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e4c2946a099d3922c054bccac03ffffbe33b934bcaba85df4c8b789a08c81252`
- **SHA1:** `4f830363fcc0b0f714b21e3248b2f450d88b93e4`
- **MD5:** `99ebfb3d09550b756b28b93483380651`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (624), with no line terminators |
| Tamaño | 624 B |
| Entropía | 5.38 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (624), with no line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://103.213.112.XXX:58691/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| ip | 103.213.112.XXX | static_analysis |
| hash | e4c2946a099d3922c054bccac03ffffbe33b934bcaba85df4c8b789a08c81252 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
