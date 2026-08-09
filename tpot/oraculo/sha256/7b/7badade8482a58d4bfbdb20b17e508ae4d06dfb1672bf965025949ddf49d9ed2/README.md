# 🧬 Payload Analysis

`7badade8482a58d4bfbdb20b17e508ae4d06dfb1672bf965025949ddf49d9ed2`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:59+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7badade8482a58d4bfbdb20b17e508ae4d06dfb1672bf965025949ddf49d9ed2`
- **SHA1:** `8116c35aeafaf674d08f957eed40d8e3509fd5df`
- **MD5:** `a1584415e9f073b715a6365ba8cc3036`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.6 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://opengraphprotocol[.]org/schema/ | strings |
| url | hxxp://www[.]facebook[.]com/2008/fbml | strings |
| url | hxxp://www[.]w3[.]org/1999/xhtml | strings |
| url | hxxp://www[.]w3[.]org/TR/xhtml1/DTD/xhtml1-transitional.dtd | strings |
| hash | 7badade8482a58d4bfbdb20b17e508ae4d06dfb1672bf965025949ddf49d9ed2 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
