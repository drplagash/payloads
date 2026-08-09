# 🧬 Payload Analysis

`d12206ee341c6db2db0afc9ff112357212d3c6af9cdb61c10ab4654707418be2`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d12206ee341c6db2db0afc9ff112357212d3c6af9cdb61c10ab4654707418be2`
- **SHA1:** `5bb017a3285980260781c618d39ec48a0170e444`
- **MD5:** `72a225cf16ce29fbcc863fc876e844ef`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text |
| Tamaño | 572 B |
| Entropía | 5.05 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2002/04/secext | strings |
| hash | d12206ee341c6db2db0afc9ff112357212d3c6af9cdb61c10ab4654707418be2 | static_analysis |
| ip | 185.16.38.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
