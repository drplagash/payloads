# 🧬 Payload Analysis

`ce1b6ec055ed5269ca73649905316f90930d1ee5191cc3b13705511056c7557a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ce1b6ec055ed5269ca73649905316f90930d1ee5191cc3b13705511056c7557a`
- **SHA1:** `97b93488a1943a459247eefba081ab6f2d5e925b`
- **MD5:** `10a47fd534499607345ddfccff2ccf7b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 425 B |
| Entropía | 5.53 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| hash | ce1b6ec055ed5269ca73649905316f90930d1ee5191cc3b13705511056c7557a | static_analysis |
| ip | 151.115.91.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
