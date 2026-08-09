# 🧬 Payload Analysis

`f6d8ad7b7e4b3e7965c3e5b97c8619be34af4a6b321517b5cc4a4c1f0e51099e`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f6d8ad7b7e4b3e7965c3e5b97c8619be34af4a6b321517b5cc4a4c1f0e51099e`
- **SHA1:** `6e027a5c5825c67382b5458657f2380e42180765`
- **MD5:** `6da5d3a804fe02369c8acc368629e8ea`

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
| hash | f6d8ad7b7e4b3e7965c3e5b97c8619be34af4a6b321517b5cc4a4c1f0e51099e | static_analysis |
| ip | 91.92.40.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
