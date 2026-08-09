# 🧬 Payload Analysis

`43c6ae8dd1301f05c6d39e702a92e10932e3757ec4b08b92c5b8a908d1f30799`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `43c6ae8dd1301f05c6d39e702a92e10932e3757ec4b08b92c5b8a908d1f30799`
- **SHA1:** `e62f7cb6a279011e78370e96f0cfd6b31c81ca62`
- **MD5:** `48bfc7bee801639d3771869c472e5d20`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.85 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 43c6ae8dd1301f05c6d39e702a92e10932e3757ec4b08b92c5b8a908d1f30799 | static_analysis |
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
