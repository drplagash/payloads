# 🧬 Payload Analysis

`3c50bb79d17ecaf2c1ed88a199bf6fcc8df474d7d9a4d44689573c6944ebb12d`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.18. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3c50bb79d17ecaf2c1ed88a199bf6fcc8df474d7d9a4d44689573c6944ebb12d`
- **SHA1:** `865ac4c6a9e40fd24a9a3cad6df31de25f38b6fd`
- **MD5:** `906a804daca8a5873d3a04ded4b9724c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.18 |
| Strings | 26 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.2; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 3c50bb79d17ecaf2c1ed88a199bf6fcc8df474d7d9a4d44689573c6944ebb12d | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

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
