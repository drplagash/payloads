# 🧬 Payload Analysis

`c00a62ca32e7f838a0b7de5771f4afb57b3e06f65f129d50d1f78f0c93f2b052`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c00a62ca32e7f838a0b7de5771f4afb57b3e06f65f129d50d1f78f0c93f2b052`
- **SHA1:** `995497ab10dbedbcbfd06a4628e103d76ef7725e`
- **MD5:** `302ec6b2b4fae763707e150821aa1fd7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 791 B |
| Entropía | 5.52 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 81.52.172.XXX | static_analysis |
| hash | c00a62ca32e7f838a0b7de5771f4afb57b3e06f65f129d50d1f78f0c93f2b052 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
