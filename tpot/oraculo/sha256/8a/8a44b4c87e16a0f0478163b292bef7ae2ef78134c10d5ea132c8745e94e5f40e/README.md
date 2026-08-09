# 🧬 Payload Analysis

`8a44b4c87e16a0f0478163b292bef7ae2ef78134c10d5ea132c8745e94e5f40e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:20+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8a44b4c87e16a0f0478163b292bef7ae2ef78134c10d5ea132c8745e94e5f40e`
- **SHA1:** `e3f1ee967d366a941b7ac1a655d33c65eaf59fab`
- **MD5:** `88aa5937b8a8f4dee72926d3d7c9818c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 707 B |
| Entropía | 5.43 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | 8a44b4c87e16a0f0478163b292bef7ae2ef78134c10d5ea132c8745e94e5f40e | static_analysis |
| ip | 89.190.156.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
