# 🧬 Payload Analysis

`18676949bf8bec8411c6e30f0c0d4a0725d9e8c11cc150c0565d504bc14ab77e`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:57+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `18676949bf8bec8411c6e30f0c0d4a0725d9e8c11cc150c0565d504bc14ab77e`
- **SHA1:** `0d884c6204b9e7d8e191dd5569a954f7a9ba56bc`
- **MD5:** `0a17f0bdbe952c1ec4a377b92f6dd1eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 21 B |
| Entropía | 4.2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 18676949bf8bec8411c6e30f0c0d4a0725d9e8c11cc150c0565d504bc14ab77e | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
