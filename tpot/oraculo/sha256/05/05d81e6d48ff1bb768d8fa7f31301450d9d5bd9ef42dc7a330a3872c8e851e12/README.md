# 🧬 Payload Analysis

`05d81e6d48ff1bb768d8fa7f31301450d9d5bd9ef42dc7a330a3872c8e851e12`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `05d81e6d48ff1bb768d8fa7f31301450d9d5bd9ef42dc7a330a3872c8e851e12`
- **SHA1:** `83539974f08bed495c3e07e12229b5b4b2176f71`
- **MD5:** `e79eecaa23f40efb27e13817a4f3ac00`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.5 |
| Strings | 36 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| ip | 89.190.156.XXX | static_analysis |
| hash | 05d81e6d48ff1bb768d8fa7f31301450d9d5bd9ef42dc7a330a3872c8e851e12 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
