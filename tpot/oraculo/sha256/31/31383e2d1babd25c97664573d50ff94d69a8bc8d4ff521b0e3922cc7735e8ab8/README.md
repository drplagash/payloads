# 🧬 Payload Analysis

`31383e2d1babd25c97664573d50ff94d69a8bc8d4ff521b0e3922cc7735e8ab8`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `31383e2d1babd25c97664573d50ff94d69a8bc8d4ff521b0e3922cc7735e8ab8`
- **SHA1:** `dab204fb1a2cb2397d25c548bbdb6e0982a3bf21`
- **MD5:** `49c9f0d1c89e69520c1117760f027550`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xeb2e76cd 20ec40c6 |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xeb2e76cd 20ec40c6; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 31383e2d1babd25c97664573d50ff94d69a8bc8d4ff521b0e3922cc7735e8ab8 | static_analysis |
| ip | 46.200.89.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
