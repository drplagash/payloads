# 🧬 Payload Analysis

`1f6b4efadaf8edebd60554862705db9766ee89a541b2af33a6c00ce9673f870c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:44+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1f6b4efadaf8edebd60554862705db9766ee89a541b2af33a6c00ce9673f870c`
- **SHA1:** `3e042fba60b03188bbaab47b13088433f1adb544`
- **MD5:** `2f9e5480a19f4c0b8c9ac7f265f77ee6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | PGP symmetric key encrypted data - salted - |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=PGP symmetric key encrypted data - salted -; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 1f6b4efadaf8edebd60554862705db9766ee89a541b2af33a6c00ce9673f870c | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

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
