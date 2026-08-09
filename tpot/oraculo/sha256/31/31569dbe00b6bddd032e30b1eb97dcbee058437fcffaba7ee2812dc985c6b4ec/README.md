# 🧬 Payload Analysis

`31569dbe00b6bddd032e30b1eb97dcbee058437fcffaba7ee2812dc985c6b4ec`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `31569dbe00b6bddd032e30b1eb97dcbee058437fcffaba7ee2812dc985c6b4ec`
- **SHA1:** `df54c614fc26a7217013db9b53c0b8e41a6d59e8`
- **MD5:** `7b853ac87447cac6a1813e1cb7de26c1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 23 B |
| Entropía | 4.26 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 31569dbe00b6bddd032e30b1eb97dcbee058437fcffaba7ee2812dc985c6b4ec | static_analysis |
| ip | 91.92.40.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
