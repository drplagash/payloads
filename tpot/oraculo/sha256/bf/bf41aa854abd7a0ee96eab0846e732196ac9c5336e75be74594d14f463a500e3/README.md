# 🧬 Payload Analysis

`bf41aa854abd7a0ee96eab0846e732196ac9c5336e75be74594d14f463a500e3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:02:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bf41aa854abd7a0ee96eab0846e732196ac9c5336e75be74594d14f463a500e3`
- **SHA1:** `98acec1e553ffb0ff3be3d31b1f9e9d93f9dec03`
- **MD5:** `28a7d3ec239f7a8e935b3be3ab8e3e68`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | bf41aa854abd7a0ee96eab0846e732196ac9c5336e75be74594d14f463a500e3 | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
