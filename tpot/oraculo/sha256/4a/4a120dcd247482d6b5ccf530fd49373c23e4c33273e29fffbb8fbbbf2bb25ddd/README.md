# 🧬 Payload Analysis

`4a120dcd247482d6b5ccf530fd49373c23e4c33273e29fffbb8fbbbf2bb25ddd`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:02:12+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4a120dcd247482d6b5ccf530fd49373c23e4c33273e29fffbb8fbbbf2bb25ddd`
- **SHA1:** `d73115f649b1c3c14b4a1ec5f86337b3ba51742c`
- **MD5:** `81d4b944ce148588ab22a53d9b9c3006`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.38 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.4; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 4a120dcd247482d6b5ccf530fd49373c23e4c33273e29fffbb8fbbbf2bb25ddd | static_analysis |
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
