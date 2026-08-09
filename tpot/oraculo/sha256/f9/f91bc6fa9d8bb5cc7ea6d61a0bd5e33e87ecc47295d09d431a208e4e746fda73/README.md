# 🧬 Payload Analysis

`f91bc6fa9d8bb5cc7ea6d61a0bd5e33e87ecc47295d09d431a208e4e746fda73`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f91bc6fa9d8bb5cc7ea6d61a0bd5e33e87ecc47295d09d431a208e4e746fda73`
- **SHA1:** `a45c9e8627dc052aee3c168097ebcce42b9548d1`
- **MD5:** `c29b684ac55b1dfd15f6d5e7e5f462f3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.52 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 153.96.249.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | f91bc6fa9d8bb5cc7ea6d61a0bd5e33e87ecc47295d09d431a208e4e746fda73 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
