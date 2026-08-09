# 🧬 Payload Analysis

`c0212436903d83fba7b2fc8b688359357d3f87d4a24e87adf8afaa0eac65ccb3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c0212436903d83fba7b2fc8b688359357d3f87d4a24e87adf8afaa0eac65ccb3`
- **SHA1:** `09a033d72f2083598baecb445b7d9ae3739749d1`
- **MD5:** `650ad8a527ae841ad552d7400b3c1b7a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 410 B |
| Entropía | 5.4 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | c0212436903d83fba7b2fc8b688359357d3f87d4a24e87adf8afaa0eac65ccb3 | static_analysis |
| ip | 87.246.54.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
