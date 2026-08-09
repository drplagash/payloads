# 🧬 Payload Analysis

`33f16582b3c3fee628ff8ed4ac134e90b8034cd84b1af6c9c914d2a85c527f8d`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:57+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `33f16582b3c3fee628ff8ed4ac134e90b8034cd84b1af6c9c914d2a85c527f8d`
- **SHA1:** `b78926fc24148d1f7b92dc7fcc00573d3c118be4`
- **MD5:** `eacd72ff8a68648520e87b88855d6afe`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 24 B |
| Entropía | 4.42 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 33f16582b3c3fee628ff8ed4ac134e90b8034cd84b1af6c9c914d2a85c527f8d | static_analysis |
| ip | 91.92.40.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
