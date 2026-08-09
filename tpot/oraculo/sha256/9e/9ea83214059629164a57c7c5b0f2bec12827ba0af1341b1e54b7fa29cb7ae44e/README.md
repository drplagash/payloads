# 🧬 Payload Analysis

`9ea83214059629164a57c7c5b0f2bec12827ba0af1341b1e54b7fa29cb7ae44e`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:17:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9ea83214059629164a57c7c5b0f2bec12827ba0af1341b1e54b7fa29cb7ae44e`
- **SHA1:** `f1f15b1fdb62f29d921849e611fd039129480be7`
- **MD5:** `130933c2b1d8c95a73eb9863f1ce3066`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 31 B |
| Entropía | 4.15 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 9ea83214059629164a57c7c5b0f2bec12827ba0af1341b1e54b7fa29cb7ae44e | static_analysis |
| ip | 216.180.246.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
