# 🧬 Payload Analysis

`79c6fa9576461ddc2b20b1bd785ca44d947bc8bc75741de507b85262d9dbde06`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `79c6fa9576461ddc2b20b1bd785ca44d947bc8bc75741de507b85262d9dbde06`
- **SHA1:** `44116c57310a1a2ecbb25215ba98892bbc396ad6`
- **MD5:** `e5c59e6eab08a5a6e95023ce589d82b6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 805 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 104.210.174.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 79c6fa9576461ddc2b20b1bd785ca44d947bc8bc75741de507b85262d9dbde06 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
