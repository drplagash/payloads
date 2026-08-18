# 🧬 Payload Analysis

`cf92c4132eeb44ce57d50aac69bf987a802560587d475b873817d3150b98d591`

## 📌 Resumen

Texto ASCII de 624 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `encoding` en `hxxp://schemas[.]xmlsoap[.]org/soap/encoding/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/cf92c4132eeb44ce57d50aac69bf987a802560587d475b873817d3150b98d591.md](../../../../../malware-like/oraculo/downloader/cf92c4132eeb44ce57d50aac69bf987a802560587d475b873817d3150b98d591.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:28:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cf92c4132eeb44ce57d50aac69bf987a802560587d475b873817d3150b98d591`
- **SHA1:** `5e434db77ed7123df2e7d033cc1dc06230ba6462`
- **MD5:** `f6691bd3a9fd48b3e121b5dc17b0c396`

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
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://203.101.186.XXX:41588/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| ip | 203.101.186.XXX | static_analysis |
| hash | cf92c4132eeb44ce57d50aac69bf987a802560587d475b873817d3150b98d591 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
