# 🧬 Payload Analysis

`96e0c217fa62369435b4e8b885bc0b13d583192ce63fa36953cf8d526bb739a4`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:46:01+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `96e0c217fa62369435b4e8b885bc0b13d583192ce63fa36953cf8d526bb739a4`
- **SHA1:** `953bae678ab76d51b15341f3ebb94c54414693c6`
- **MD5:** `4b56804034b5a223d6a6e5ae74cbd283`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | IRIS Showcase template - version -119 |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=IRIS Showcase template - version -119; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 96e0c217fa62369435b4e8b885bc0b13d583192ce63fa36953cf8d526bb739a4 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
