# 🧬 Payload Analysis

`255e70b913a4b1d9d078180a0fa164cc67f6d3a5917b39e0804ef91acf42f7ce`

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

- **SHA256:** `255e70b913a4b1d9d078180a0fa164cc67f6d3a5917b39e0804ef91acf42f7ce`
- **SHA1:** `2e2269074c4fe767a72458e45b0d7213a20016b9`
- **MD5:** `247b22f40244ae9243047c2c594b2580`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 255e70b913a4b1d9d078180a0fa164cc67f6d3a5917b39e0804ef91acf42f7ce | static_analysis |
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
