# 🧬 Payload Analysis

`b3492e796b4afc93d4080a87e1173b98030e2b1d18cf8c29d36db9505f8adae7`

## 📌 Resumen

Texto ASCII de 535 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `XMLSchema-instance` en `hxxp://www[.]w3[.]org/2001/XMLSchema-instance`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b3492e796b4afc93d4080a87e1173b98030e2b1d18cf8c29d36db9505f8adae7.md](../../../../../malware-like/oraculo/downloader/b3492e796b4afc93d4080a87e1173b98030e2b1d18cf8c29d36db9505f8adae7.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b3492e796b4afc93d4080a87e1173b98030e2b1d18cf8c29d36db9505f8adae7`
- **SHA1:** `866eed24f6ebfff2ae6d5c46cd0d0a1f9f981f5e`
- **MD5:** `4bc3c467ba5d00b3c96cb48a56cddd9c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (531), with CRLF line terminators |
| Tamaño | 535 B |
| Entropía | 5.16 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (531), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema-instance | strings |
| url | hxxp://purenetworks[.]com/HNAP1/ | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | b3492e796b4afc93d4080a87e1173b98030e2b1d18cf8c29d36db9505f8adae7 | static_analysis |
| ip | 38.100.221.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
