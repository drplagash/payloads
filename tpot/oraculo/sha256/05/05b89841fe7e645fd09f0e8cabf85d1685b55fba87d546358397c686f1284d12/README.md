# 🧬 Payload Analysis

`05b89841fe7e645fd09f0e8cabf85d1685b55fba87d546358397c686f1284d12`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `05b89841fe7e645fd09f0e8cabf85d1685b55fba87d546358397c686f1284d12`
- **SHA1:** `c161f7c0ca69aef152a5dad2134bbce2a5209085`
- **MD5:** `0b7dd0526bbc68a2ce14f0a8605dc577`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 24 B |
| Entropía | 4.33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 05b89841fe7e645fd09f0e8cabf85d1685b55fba87d546358397c686f1284d12 | static_analysis |
| ip | 213.177.179.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
