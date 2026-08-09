# 🧬 Payload Analysis

`0537d74209c6a7e05bea9ea3e810df77330da670e68c9e5cbc93006ef018e742`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:06+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0537d74209c6a7e05bea9ea3e810df77330da670e68c9e5cbc93006ef018e742`
- **SHA1:** `13e4e2ee93610667d75f727d459642ec46b1876b`
- **MD5:** `2b4af8123b4dc3280ddc404f3ba5ce46`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 399 B |
| Entropía | 5.37 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 103.123.226.XXX | static_analysis |
| ip | 190.179.128.XXX | static_analysis |
| hash | 0537d74209c6a7e05bea9ea3e810df77330da670e68c9e5cbc93006ef018e742 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
