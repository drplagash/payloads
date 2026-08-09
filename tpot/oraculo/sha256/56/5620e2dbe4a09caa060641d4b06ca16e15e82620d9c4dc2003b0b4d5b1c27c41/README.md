# 🧬 Payload Analysis

`5620e2dbe4a09caa060641d4b06ca16e15e82620d9c4dc2003b0b4d5b1c27c41`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:08:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5620e2dbe4a09caa060641d4b06ca16e15e82620d9c4dc2003b0b4d5b1c27c41`
- **SHA1:** `a17ac4dbc1a5a6540582a6b894b86437ec96e924`
- **MD5:** `c5eb80893ac10dec2e4095faf4a29d6e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 518 B |
| Entropía | 5.44 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 5620e2dbe4a09caa060641d4b06ca16e15e82620d9c4dc2003b0b4d5b1c27c41 | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
