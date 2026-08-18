# 🧬 Payload Analysis

`100530c9ea8788a4979a286a77bd92a657d3720095bd5111fb8f2c9e48b386bd`

## 📌 Resumen

Artefacto de 548 B. Entropía registrada: 5.37. Las detecciones YARA incluyen `Big_Numbers1`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Yara signature match. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:43:28.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `100530c9ea8788a4979a286a77bd92a657d3720095bd5111fb8f2c9e48b386bd`
- **MD5:** `1987ba5aa4a5c9033c4c4bfb486684d5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.37 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Yara signature match**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; yara_matches=1; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 100530c9ea8788a4979a286a77bd92a657d3720095bd5111fb8f2c9e48b386bd | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
