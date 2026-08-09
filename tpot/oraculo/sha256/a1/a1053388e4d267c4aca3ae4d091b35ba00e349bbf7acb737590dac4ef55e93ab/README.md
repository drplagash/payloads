# 🧬 Payload Analysis

`a1053388e4d267c4aca3ae4d091b35ba00e349bbf7acb737590dac4ef55e93ab`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a1053388e4d267c4aca3ae4d091b35ba00e349bbf7acb737590dac4ef55e93ab`
- **SHA1:** `4146a2f71774532a00d5b961dd3aeaffe6bc8422`
- **MD5:** `d86273fe5a767dd4bff9d60b742bf397`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 177 B |
| Entropía | 5.15 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| hash | a1053388e4d267c4aca3ae4d091b35ba00e349bbf7acb737590dac4ef55e93ab | static_analysis |
| ip | 160.119.76.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
