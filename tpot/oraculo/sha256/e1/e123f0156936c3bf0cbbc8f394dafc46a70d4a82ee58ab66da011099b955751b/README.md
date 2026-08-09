# 🧬 Payload Analysis

`e123f0156936c3bf0cbbc8f394dafc46a70d4a82ee58ab66da011099b955751b`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:06:31+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e123f0156936c3bf0cbbc8f394dafc46a70d4a82ee58ab66da011099b955751b`
- **SHA1:** `593e709a921eacd8decd55cb5b28635ba40dc053`
- **MD5:** `58869f553d7cea4c8ae202be2d7ea7f1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with no line terminators |
| Tamaño | 93 B |
| Entropía | 4.96 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=XML 1.0 document, ASCII text, with no line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | e123f0156936c3bf0cbbc8f394dafc46a70d4a82ee58ab66da011099b955751b | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
