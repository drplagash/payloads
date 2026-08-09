# 🧬 Payload Analysis

`0e8cf429d598832ce1e5de4f631ff3f7e1734867b55790090755de8734cf8402`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0e8cf429d598832ce1e5de4f631ff3f7e1734867b55790090755de8734cf8402`
- **SHA1:** `07e1224615ec38226f4e365f0837a334c91bfe4b`
- **MD5:** `58e402f3c6f6fb08fe8bc070c7b1fd96`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 803 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 101.214.207.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 0e8cf429d598832ce1e5de4f631ff3f7e1734867b55790090755de8734cf8402 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
