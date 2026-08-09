# 🧬 Payload Analysis

`2ac16e95ad9f816a44d9941565ad3bf18cc89426fa82e3e1df1c517e32a9ca6c`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:33:39+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2ac16e95ad9f816a44d9941565ad3bf18cc89426fa82e3e1df1c517e32a9ca6c`
- **SHA1:** `928da0d631c49a08dab4be59bb05c2d90a698c0e`
- **MD5:** `eda0ce810aee0f1b1a164b475a8ac3ef`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 180 B |
| Entropía | 5.35 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 2ac16e95ad9f816a44d9941565ad3bf18cc89426fa82e3e1df1c517e32a9ca6c | static_analysis |
| ip | 213.209.159.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
