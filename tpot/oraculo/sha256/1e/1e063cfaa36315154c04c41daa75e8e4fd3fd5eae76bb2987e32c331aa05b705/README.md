# 🧬 Payload Analysis

`1e063cfaa36315154c04c41daa75e8e4fd3fd5eae76bb2987e32c331aa05b705`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.11. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:02:12.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1e063cfaa36315154c04c41daa75e8e4fd3fd5eae76bb2987e32c331aa05b705`
- **SHA1:** `16cd4db41d51eedd8c1e784b2fef8a568e6f15da`
- **MD5:** `2ca262b008efcbcba817932985234b55`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.11 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.1; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 1e063cfaa36315154c04c41daa75e8e4fd3fd5eae76bb2987e32c331aa05b705 | static_analysis |
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
