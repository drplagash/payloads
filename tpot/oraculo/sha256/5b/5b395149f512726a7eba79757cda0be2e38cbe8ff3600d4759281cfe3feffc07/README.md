# 🧬 Payload Analysis

`5b395149f512726a7eba79757cda0be2e38cbe8ff3600d4759281cfe3feffc07`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5b395149f512726a7eba79757cda0be2e38cbe8ff3600d4759281cfe3feffc07`
- **SHA1:** `93390260f70edddbe411abfe6000f22fcfc11ab4`
- **MD5:** `8ab69f433ba79f2d249300f0b4f49bd1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 97 B |
| Entropía | 5 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 239.255.255.XXX | static_analysis |
| hash | 5b395149f512726a7eba79757cda0be2e38cbe8ff3600d4759281cfe3feffc07 | static_analysis |
| ip | 91.236.116.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
