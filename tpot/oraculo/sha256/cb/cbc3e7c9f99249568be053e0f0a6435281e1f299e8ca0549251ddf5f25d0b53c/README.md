# 🧬 Payload Analysis

`cbc3e7c9f99249568be053e0f0a6435281e1f299e8ca0549251ddf5f25d0b53c`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:05+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cbc3e7c9f99249568be053e0f0a6435281e1f299e8ca0549251ddf5f25d0b53c`
- **SHA1:** `a7edfc1e029135992841ccf4d177d9cb90045bbc`
- **MD5:** `d660cb72b6290de4fe048c7d994f5623`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 27 B |
| Entropía | 4.36 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | cbc3e7c9f99249568be053e0f0a6435281e1f299e8ca0549251ddf5f25d0b53c | static_analysis |
| ip | 213.209.159.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
