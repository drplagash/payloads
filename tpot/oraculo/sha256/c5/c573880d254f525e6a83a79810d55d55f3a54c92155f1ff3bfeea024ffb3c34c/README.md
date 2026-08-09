# 🧬 Payload Analysis

`c573880d254f525e6a83a79810d55d55f3a54c92155f1ff3bfeea024ffb3c34c`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:00:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c573880d254f525e6a83a79810d55d55f3a54c92155f1ff3bfeea024ffb3c34c`
- **SHA1:** `d98115fb6ef2568363815780ac02e99f704f8e0b`
- **MD5:** `29c5322a7c2ac2fe335ac83989123293`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 52 B |
| Entropía | 4.7 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c573880d254f525e6a83a79810d55d55f3a54c92155f1ff3bfeea024ffb3c34c | static_analysis |
| ip | 195.178.110.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
