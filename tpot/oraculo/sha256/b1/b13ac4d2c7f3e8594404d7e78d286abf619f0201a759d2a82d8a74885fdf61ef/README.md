# 🧬 Payload Analysis

`b13ac4d2c7f3e8594404d7e78d286abf619f0201a759d2a82d8a74885fdf61ef`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:57:27+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b13ac4d2c7f3e8594404d7e78d286abf619f0201a759d2a82d8a74885fdf61ef`
- **SHA1:** `8ee6b31aaa43809143e144bf20cdbdbb2a0d5ed2`
- **MD5:** `5992138266447b7c88e3f5d57fa8d006`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, ASCII text, with CRLF, LF line terminators |
| Tamaño | 266 B |
| Entropía | 5.04 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=HTML document, ASCII text, with CRLF, LF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | b13ac4d2c7f3e8594404d7e78d286abf619f0201a759d2a82d8a74885fdf61ef | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
