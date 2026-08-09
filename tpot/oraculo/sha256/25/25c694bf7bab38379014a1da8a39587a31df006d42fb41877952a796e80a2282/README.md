# 🧬 Payload Analysis

`25c694bf7bab38379014a1da8a39587a31df006d42fb41877952a796e80a2282`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `25c694bf7bab38379014a1da8a39587a31df006d42fb41877952a796e80a2282`
- **SHA1:** `e0912fb0cae6dc3ce53734ae41ce400d4329190f`
- **MD5:** `66c8f98e665eb04bb3299264b7618ad8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, ASCII text, with very long lines (382) |
| Tamaño | 1.4 KiB |
| Entropía | 4.92 |
| Strings | 28 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=HTML document, ASCII text, with very long lines (382); iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 25c694bf7bab38379014a1da8a39587a31df006d42fb41877952a796e80a2282 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
