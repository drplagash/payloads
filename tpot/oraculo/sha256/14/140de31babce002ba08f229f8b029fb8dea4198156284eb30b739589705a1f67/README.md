# 🧬 Payload Analysis

`140de31babce002ba08f229f8b029fb8dea4198156284eb30b739589705a1f67`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:03:26+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `140de31babce002ba08f229f8b029fb8dea4198156284eb30b739589705a1f67`
- **SHA1:** `4bb51ea52e9118c80fda0dd2cb498652a63bbd7d`
- **MD5:** `1731abe47b09388d1fa7022792d5b807`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | MPEG-4 LOAS |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=MPEG-4 LOAS; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 140de31babce002ba08f229f8b029fb8dea4198156284eb30b739589705a1f67 | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | media or resource |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
