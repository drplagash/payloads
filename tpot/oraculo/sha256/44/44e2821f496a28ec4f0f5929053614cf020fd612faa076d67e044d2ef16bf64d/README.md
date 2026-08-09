# 🧬 Payload Analysis

`44e2821f496a28ec4f0f5929053614cf020fd612faa076d67e044d2ef16bf64d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `44e2821f496a28ec4f0f5929053614cf020fd612faa076d67e044d2ef16bf64d`
- **SHA1:** `0458cbca66b2a9f8e8ba17501c7cecfe8e56f00b`
- **MD5:** `66d4496ab5f004f4dde10a9f3aad2b79`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 349 B |
| Entropía | 5.39 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| hash | 44e2821f496a28ec4f0f5929053614cf020fd612faa076d67e044d2ef16bf64d | static_analysis |
| ip | 185.93.89.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
