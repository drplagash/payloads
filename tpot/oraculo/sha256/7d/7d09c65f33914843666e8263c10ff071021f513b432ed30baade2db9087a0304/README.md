# 🧬 Payload Analysis

`7d09c65f33914843666e8263c10ff071021f513b432ed30baade2db9087a0304`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7d09c65f33914843666e8263c10ff071021f513b432ed30baade2db9087a0304`
- **SHA1:** `0943dc997d9e32009fcc6c411335bcbad3508405`
- **MD5:** `9700837d1741c5f2ca2dc7d43edc90f8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | PRCS packaged project |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=PRCS packaged project; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 7d09c65f33914843666e8263c10ff071021f513b432ed30baade2db9087a0304 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
