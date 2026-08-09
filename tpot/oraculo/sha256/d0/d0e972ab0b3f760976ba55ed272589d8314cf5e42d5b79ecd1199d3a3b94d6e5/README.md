# 🧬 Payload Analysis

`d0e972ab0b3f760976ba55ed272589d8314cf5e42d5b79ecd1199d3a3b94d6e5`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d0e972ab0b3f760976ba55ed272589d8314cf5e42d5b79ecd1199d3a3b94d6e5`
- **SHA1:** `95708d550906507532a4fc22c2705bbe1c543f59`
- **MD5:** `3ebadc66e1e57a8ed0f2a5241b656d12`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 117 B |
| Entropía | 4.96 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| hash | d0e972ab0b3f760976ba55ed272589d8314cf5e42d5b79ecd1199d3a3b94d6e5 | static_analysis |
| ip | 139.59.149.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
