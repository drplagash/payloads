# 🧬 Payload Analysis

`6ab56f3b90b11b93e1e0e86bfa7613445683aad1e759a5ea57a8ed11701ba5f6`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6ab56f3b90b11b93e1e0e86bfa7613445683aad1e759a5ea57a8ed11701ba5f6`
- **SHA1:** `649dedbccc2e3fc032fa495f30d43d317bfca180`
- **MD5:** `48db6cc47ab34887201e8c1f7a37714c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.5 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 115.22.218.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 6ab56f3b90b11b93e1e0e86bfa7613445683aad1e759a5ea57a8ed11701ba5f6 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
