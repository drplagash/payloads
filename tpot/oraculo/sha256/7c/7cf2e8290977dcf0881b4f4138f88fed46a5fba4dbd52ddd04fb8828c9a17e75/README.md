# 🧬 Payload Analysis

`7cf2e8290977dcf0881b4f4138f88fed46a5fba4dbd52ddd04fb8828c9a17e75`

## 📌 Resumen

Texto ASCII de 624 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `envelope` en `hxxp://schemas[.]xmlsoap[.]org/soap/envelope/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/7cf2e8290977dcf0881b4f4138f88fed46a5fba4dbd52ddd04fb8828c9a17e75.md](../../../../../malware-like/oraculo/downloader/7cf2e8290977dcf0881b4f4138f88fed46a5fba4dbd52ddd04fb8828c9a17e75.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7cf2e8290977dcf0881b4f4138f88fed46a5fba4dbd52ddd04fb8828c9a17e75`
- **SHA1:** `9782f3cf206fc740b437262941e0a8b34261cc45`
- **MD5:** `3e059bc435106674ae5faa322f328b0c`

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
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://139.135.59.XXX:36773/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| ip | 139.135.59.XXX | static_analysis |
| hash | 7cf2e8290977dcf0881b4f4138f88fed46a5fba4dbd52ddd04fb8828c9a17e75 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
