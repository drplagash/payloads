# 🧬 Payload Analysis

`22fb5ebe301ff2fca52bffea4c8e7b2703e12284681bfbd687cb6d2e070ac19a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:59+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `22fb5ebe301ff2fca52bffea4c8e7b2703e12284681bfbd687cb6d2e070ac19a`
- **SHA1:** `a1b12116048400f3587e7e73ca7d72cb20ab7cc8`
- **MD5:** `a531abe7ba4400fc10b0913ad60cbbcd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 108 B |
| Entropía | 4.93 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | 22fb5ebe301ff2fca52bffea4c8e7b2703e12284681bfbd687cb6d2e070ac19a | static_analysis |
| ip | 161.35.203.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
