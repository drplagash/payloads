# 🧬 Payload Analysis

`db17989890606a158c3ee73002859ae476cd2c7f562f7c263e8cd028cee3cc15`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `db17989890606a158c3ee73002859ae476cd2c7f562f7c263e8cd028cee3cc15`
- **SHA1:** `4599f11aaffeeb62e0dd96642d546204186eb09a`
- **MD5:** `46870d03150f36374a398725c20d6d05`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 791 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.15.88.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | db17989890606a158c3ee73002859ae476cd2c7f562f7c263e8cd028cee3cc15 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
