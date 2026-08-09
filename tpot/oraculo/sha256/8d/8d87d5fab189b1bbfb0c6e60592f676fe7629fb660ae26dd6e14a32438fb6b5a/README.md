# 🧬 Payload Analysis

`8d87d5fab189b1bbfb0c6e60592f676fe7629fb660ae26dd6e14a32438fb6b5a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:09:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8d87d5fab189b1bbfb0c6e60592f676fe7629fb660ae26dd6e14a32438fb6b5a`
- **SHA1:** `691164f35ece219405ea48c6815de337c7dee9e3`
- **MD5:** `eea8c0471a7d3dbc60bdab1413b409e5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 101 B |
| Entropía | 5.11 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.172.XXX | static_analysis |
| hash | 8d87d5fab189b1bbfb0c6e60592f676fe7629fb660ae26dd6e14a32438fb6b5a | static_analysis |
| ip | 93.123.72.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
