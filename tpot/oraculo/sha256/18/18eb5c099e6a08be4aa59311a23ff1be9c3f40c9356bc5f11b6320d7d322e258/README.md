# 🧬 Payload Analysis

`18eb5c099e6a08be4aa59311a23ff1be9c3f40c9356bc5f11b6320d7d322e258`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `18eb5c099e6a08be4aa59311a23ff1be9c3f40c9356bc5f11b6320d7d322e258`
- **SHA1:** `53f1d10487c291c2b985ae9156c2923e576ad216`
- **MD5:** `676944fd4ab0a22a3ddc903b90c12dec`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 68 B |
| Entropía | 4.68 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 18eb5c099e6a08be4aa59311a23ff1be9c3f40c9356bc5f11b6320d7d322e258 | static_analysis |
| ip | 176.65.139.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
