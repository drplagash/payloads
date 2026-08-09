# 🧬 Payload Analysis

`cc5f813eaf7e7dab4c7dd80108c7c3feeee0187198f935ffce0d5773d682e67d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cc5f813eaf7e7dab4c7dd80108c7c3feeee0187198f935ffce0d5773d682e67d`
- **SHA1:** `8ad927137473d8832542b11ea3b096fbc84731d1`
- **MD5:** `d3792ddc22ca70ed573f04cfd03a16e5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 734 B |
| Entropía | 5.35 |
| Strings | 22 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | cc5f813eaf7e7dab4c7dd80108c7c3feeee0187198f935ffce0d5773d682e67d | static_analysis |
| ip | 87.106.98.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
