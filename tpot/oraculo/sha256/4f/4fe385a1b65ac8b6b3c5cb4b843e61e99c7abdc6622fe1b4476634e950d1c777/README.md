# 🧬 Payload Analysis

`4fe385a1b65ac8b6b3c5cb4b843e61e99c7abdc6622fe1b4476634e950d1c777`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4fe385a1b65ac8b6b3c5cb4b843e61e99c7abdc6622fe1b4476634e950d1c777`
- **SHA1:** `bb8845ca29f7706dd7d83e77c6633b93dfa2162f`
- **MD5:** `1be1afab98ff6a9f86500818d26ee916`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 130 B |
| Entropía | 5.15 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| hash | 4fe385a1b65ac8b6b3c5cb4b843e61e99c7abdc6622fe1b4476634e950d1c777 | static_analysis |
| ip | 220.181.1.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
