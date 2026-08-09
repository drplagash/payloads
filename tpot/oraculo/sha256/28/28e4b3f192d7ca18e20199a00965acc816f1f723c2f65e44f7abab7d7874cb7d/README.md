# 🧬 Payload Analysis

`28e4b3f192d7ca18e20199a00965acc816f1f723c2f65e44f7abab7d7874cb7d`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `28e4b3f192d7ca18e20199a00965acc816f1f723c2f65e44f7abab7d7874cb7d`
- **SHA1:** `68fd5fbcbcd7fa337f756f2699c1dcb20b8372a3`
- **MD5:** `254b56a320c377f9a2178bf9ec62997e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 97 B |
| Entropía | 5.01 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 239.255.255.XXX | static_analysis |
| hash | 28e4b3f192d7ca18e20199a00965acc816f1f723c2f65e44f7abab7d7874cb7d | static_analysis |
| ip | 205.210.31.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
