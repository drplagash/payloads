# 🧬 Payload Analysis

`fdeb8010785a222b2459c19c8c3d4e8d411101f6294d11eb3615a886482b5744`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fdeb8010785a222b2459c19c8c3d4e8d411101f6294d11eb3615a886482b5744`
- **SHA1:** `005267d59f13aaddc37049b2e3b6f49869ea8955`
- **MD5:** `d4cb232d2e7d87b23a625369b236ba73`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 549 B |
| Entropía | 5.38 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | fdeb8010785a222b2459c19c8c3d4e8d411101f6294d11eb3615a886482b5744 | static_analysis |
| ip | 141.98.11.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
