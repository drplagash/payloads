# 🧬 Payload Analysis

`89f64a6eb67faf3471ba9c6e33331eacdfa73ab94662c0ff259ccd288a84e04e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `89f64a6eb67faf3471ba9c6e33331eacdfa73ab94662c0ff259ccd288a84e04e`
- **SHA1:** `298e93f0b1ff48ef12501ccd970db5240663d7dc`
- **MD5:** `6687790bbc6164716ed313c4bc261043`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 105 B |
| Entropía | 4.99 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.130.XXX | static_analysis |
| hash | 89f64a6eb67faf3471ba9c6e33331eacdfa73ab94662c0ff259ccd288a84e04e | static_analysis |
| ip | 183.239.58.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
