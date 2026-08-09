# 🧬 Payload Analysis

`0e5fec8a712484fbc74fd2a593d2578fceb757907e24efefa65f32f990c56ef1`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:19+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0e5fec8a712484fbc74fd2a593d2578fceb757907e24efefa65f32f990c56ef1`
- **SHA1:** `b1e48a637148ec640371cb70416993d8c7bc8dc5`
- **MD5:** `2671d6ca32aad5ace4a69b6182e0f837`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 797 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 19.173.42.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 0e5fec8a712484fbc74fd2a593d2578fceb757907e24efefa65f32f990c56ef1 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
