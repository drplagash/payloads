# 🧬 Payload Analysis

`4797f3151044535baca1a6a8320dbc075a436404c5121d0207ed4791c57b10c9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: High entropy obfuscation, Binary execution. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:03:26+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4797f3151044535baca1a6a8320dbc075a436404c5121d0207ed4791c57b10c9`
- **SHA1:** `b9fa45520dad9dbc993bb0a846bfadf50564835b`
- **MD5:** `29a3c5ff4ba083660d6a01ef1320ab7c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xeb06faac d3c8f60c |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 10 |

## 🧠 Comportamiento observado

1. **High entropy obfuscation**
2. **Binary execution**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xeb06faac d3c8f60c; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 4797f3151044535baca1a6a8320dbc075a436404c5121d0207ed4791c57b10c9 | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

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
