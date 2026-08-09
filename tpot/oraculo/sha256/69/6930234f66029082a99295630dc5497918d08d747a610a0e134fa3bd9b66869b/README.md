# 🧬 Payload Analysis

`6930234f66029082a99295630dc5497918d08d747a610a0e134fa3bd9b66869b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6930234f66029082a99295630dc5497918d08d747a610a0e134fa3bd9b66869b`
- **SHA1:** `556fe75e066939d29534508e6e51a93f302c6296`
- **MD5:** `8444f62011c3e58e1b1d619fbcc3d48e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 209 B |
| Entropía | 5.36 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 136.0.0.XXX | static_analysis |
| ip | 190.179.128.XXX | static_analysis |
| hash | 6930234f66029082a99295630dc5497918d08d747a610a0e134fa3bd9b66869b | static_analysis |
| ip | 52.200.76.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
