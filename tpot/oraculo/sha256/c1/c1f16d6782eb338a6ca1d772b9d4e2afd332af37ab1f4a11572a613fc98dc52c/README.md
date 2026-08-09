# 🧬 Payload Analysis

`c1f16d6782eb338a6ca1d772b9d4e2afd332af37ab1f4a11572a613fc98dc52c`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c1f16d6782eb338a6ca1d772b9d4e2afd332af37ab1f4a11572a613fc98dc52c`
- **SHA1:** `b90189512159435d09bda1ba5ef687ac2a84954b`
- **MD5:** `5bb11f5382eba7c3737dc9c35560d8de`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 122 B |
| Entropía | 5.07 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| url | hxxp://190.179.160.XXX:80/cgi-bin/index2.asp | strings |
| hash | c1f16d6782eb338a6ca1d772b9d4e2afd332af37ab1f4a11572a613fc98dc52c | static_analysis |
| ip | 45.205.1.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
