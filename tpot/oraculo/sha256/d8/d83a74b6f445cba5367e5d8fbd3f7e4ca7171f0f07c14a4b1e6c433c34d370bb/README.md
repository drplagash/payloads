# 🧬 Payload Analysis

`d83a74b6f445cba5367e5d8fbd3f7e4ca7171f0f07c14a4b1e6c433c34d370bb`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:29:35+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d83a74b6f445cba5367e5d8fbd3f7e4ca7171f0f07c14a4b1e6c433c34d370bb`
- **SHA1:** `17cd5c8f2b03c60b2f849e50704a7e141cd00c34`
- **MD5:** `cf0f47b5577ffe2c6b5aad0a44cbb936`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 176 B |
| Entropía | 5.1 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | d83a74b6f445cba5367e5d8fbd3f7e4ca7171f0f07c14a4b1e6c433c34d370bb | static_analysis |
| ip | 45.95.147.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
