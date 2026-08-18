# 🧬 Payload Analysis

`40359f64f11d20449544003ecc2fdc4fd7c6d5471b0e7b7783473aae95a937a3`

## 📌 Resumen

Texto ASCII de 194 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `genomecrawler` en `hxxps://www[.]nokia[.]com/genomecrawler`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/40359f64f11d20449544003ecc2fdc4fd7c6d5471b0e7b7783473aae95a937a3.md](../../../../../malware-like/oraculo/downloader/40359f64f11d20449544003ecc2fdc4fd7c6d5471b0e7b7783473aae95a937a3.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `40359f64f11d20449544003ecc2fdc4fd7c6d5471b0e7b7783473aae95a937a3`
- **SHA1:** `e1e52da71d0ea9a5f8451b8c9b125f5aa99582b6`
- **MD5:** `94065b3c55b7a7decac791ff68c8b07d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 194 B |
| Entropía | 5.24 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://www[.]nokia[.]com/genomecrawler) | strings |
| ip | 190.179.166.XXX | static_analysis |
| hash | 40359f64f11d20449544003ecc2fdc4fd7c6d5471b0e7b7783473aae95a937a3 | static_analysis |
| ip | 216.180.246.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
