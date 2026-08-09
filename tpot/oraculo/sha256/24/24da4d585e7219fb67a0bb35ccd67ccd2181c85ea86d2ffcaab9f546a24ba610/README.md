# 🧬 Payload Analysis

`24da4d585e7219fb67a0bb35ccd67ccd2181c85ea86d2ffcaab9f546a24ba610`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:05+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `24da4d585e7219fb67a0bb35ccd67ccd2181c85ea86d2ffcaab9f546a24ba610`
- **SHA1:** `6815c6d62e253084a41193fa103e7361f6786830`
- **MD5:** `a88fa2e868885750ed677306894a7b09`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 620 B |
| Entropía | 5.55 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 124.0.0.XXX | static_analysis |
| hash | 24da4d585e7219fb67a0bb35ccd67ccd2181c85ea86d2ffcaab9f546a24ba610 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
