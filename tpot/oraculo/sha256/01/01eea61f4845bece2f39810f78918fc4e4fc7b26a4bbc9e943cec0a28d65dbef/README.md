# 🧬 Payload Analysis

`01eea61f4845bece2f39810f78918fc4e4fc7b26a4bbc9e943cec0a28d65dbef`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:44+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `01eea61f4845bece2f39810f78918fc4e4fc7b26a4bbc9e943cec0a28d65dbef`
- **SHA1:** `41c7d2dc07179155b55d04089b6bab5ad50cbeb3`
- **MD5:** `4e29f50ee48ce0ac6dc9ebaf8c90070b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 118 B |
| Entropía | 4.89 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | 01eea61f4845bece2f39810f78918fc4e4fc7b26a4bbc9e943cec0a28d65dbef | static_analysis |
| ip | 198.199.89.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
