# 🧬 Payload Analysis

`b1f086e24a9700f5cffb8c8cc9484ad13132be40a411904d2c4fd579a54680ff`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:20:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b1f086e24a9700f5cffb8c8cc9484ad13132be40a411904d2c4fd579a54680ff`
- **SHA1:** `1e64ca7b2d357c74cf11bdfbb2676dde72908f4a`
- **MD5:** `de5de030671ddf56dbeaf2b61632356e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 118 B |
| Entropía | 4.97 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | b1f086e24a9700f5cffb8c8cc9484ad13132be40a411904d2c4fd579a54680ff | static_analysis |
| ip | 198.199.89.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
