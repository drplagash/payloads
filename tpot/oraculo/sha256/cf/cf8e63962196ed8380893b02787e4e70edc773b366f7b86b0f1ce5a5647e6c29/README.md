# 🧬 Payload Analysis

`cf8e63962196ed8380893b02787e4e70edc773b366f7b86b0f1ce5a5647e6c29`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cf8e63962196ed8380893b02787e4e70edc773b366f7b86b0f1ce5a5647e6c29`
- **SHA1:** `72ccdc1551a3156f114c246f350c1e38e22fe178`
- **MD5:** `9f6bc787633cf57d6a9439688a4333c2`

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
| hash | cf8e63962196ed8380893b02787e4e70edc773b366f7b86b0f1ce5a5647e6c29 | static_analysis |
| ip | 91.92.40.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
