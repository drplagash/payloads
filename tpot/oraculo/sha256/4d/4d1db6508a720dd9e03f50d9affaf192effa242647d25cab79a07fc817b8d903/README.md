# 🧬 Payload Analysis

`4d1db6508a720dd9e03f50d9affaf192effa242647d25cab79a07fc817b8d903`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:05+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4d1db6508a720dd9e03f50d9affaf192effa242647d25cab79a07fc817b8d903`
- **SHA1:** `94a5dc2edc5f1b4b6f4361709aacfb31a22f55d9`
- **MD5:** `11ec9f4d6f38206be798db82bfd21c21`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key Version 2, Created Mon Nov 17 21:14:28 2003, Unknown Algorithm (0x84) |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key Version 2, Created Mon Nov 17 21:14:28 2003, Unknown Algorithm (0x84); high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 4d1db6508a720dd9e03f50d9affaf192effa242647d25cab79a07fc817b8d903 | static_analysis |
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
