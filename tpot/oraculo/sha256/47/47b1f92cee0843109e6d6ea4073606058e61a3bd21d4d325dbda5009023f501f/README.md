# 🧬 Payload Analysis

`47b1f92cee0843109e6d6ea4073606058e61a3bd21d4d325dbda5009023f501f`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:37:19+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `47b1f92cee0843109e6d6ea4073606058e61a3bd21d4d325dbda5009023f501f`
- **MD5:** `34482085100900eb55a781c9715ef3e8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 948 B |
| Entropía | 5.62 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 134.0.0.XXX | static_analysis |
| ip | 190.179.174.XXX | static_analysis |
| hash | 47b1f92cee0843109e6d6ea4073606058e61a3bd21d4d325dbda5009023f501f | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
