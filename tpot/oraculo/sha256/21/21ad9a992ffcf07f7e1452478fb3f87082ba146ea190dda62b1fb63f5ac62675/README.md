# 🧬 Payload Analysis

`21ad9a992ffcf07f7e1452478fb3f87082ba146ea190dda62b1fb63f5ac62675`

## 📌 Resumen

Artefacto identificado como XML 1.0 document, ASCII text, with very long lines (775), with no line terminators de 775 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `icy.sh` en `hxxp://109.104.153.XXX/icy.sh`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:20:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `21ad9a992ffcf07f7e1452478fb3f87082ba146ea190dda62b1fb63f5ac62675`
- **SHA1:** `8d3bc1038210dbc5c788ae70b0043cb1ad285d51`
- **MD5:** `e0cc5d5cc4d2e5d63dfec0aa4562c7fb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (775), with no line terminators |
| Tamaño | 775 B |
| Entropía | 5.25 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (775), with no line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://109.104.153.XXX/icy.sh | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| ip | 109.104.153.XXX | static_analysis |
| hash | 21ad9a992ffcf07f7e1452478fb3f87082ba146ea190dda62b1fb63f5ac62675 | static_analysis |
| ip | 103.96.140.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
