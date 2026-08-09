# 🧬 Payload Analysis

`d25dd473bb0fc0c5e1d1e2ce8b0f0d145a27769d72db084bbc90965d9de552fc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d25dd473bb0fc0c5e1d1e2ce8b0f0d145a27769d72db084bbc90965d9de552fc`
- **SHA1:** `c1d9fcb112c64fdd809bcf4133f1469de48fd209`
- **MD5:** `dbf397ce9b47f8c057ec0fd28b3eb4e8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.48 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 137.41.191.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | d25dd473bb0fc0c5e1d1e2ce8b0f0d145a27769d72db084bbc90965d9de552fc | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
