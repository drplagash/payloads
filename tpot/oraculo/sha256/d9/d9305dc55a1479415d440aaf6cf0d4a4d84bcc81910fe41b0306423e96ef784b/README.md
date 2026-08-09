# 🧬 Payload Analysis

`d9305dc55a1479415d440aaf6cf0d4a4d84bcc81910fe41b0306423e96ef784b`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d9305dc55a1479415d440aaf6cf0d4a4d84bcc81910fe41b0306423e96ef784b`
- **SHA1:** `b1e8b05ae3b76b1206b1598a495aa711e7ad57ca`
- **MD5:** `57fb404a32ac1a821b9789ebd2ea0692`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 76 B |
| Entropía | 4.72 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d9305dc55a1479415d440aaf6cf0d4a4d84bcc81910fe41b0306423e96ef784b | static_analysis |
| ip | 36.50.135.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
