# 🧬 Payload Analysis

`cf94ecc0c4b72d8dd7853d3d8a6c5157127528c408ac9be8b8d51d559ea33970`

## 📌 Resumen

Artefacto de 1.4 KiB. Entropía registrada: 7.17. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:18:27.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cf94ecc0c4b72d8dd7853d3d8a6c5157127528c408ac9be8b8d51d559ea33970`
- **SHA1:** `2e55e2434d5a586e333306cc0b8fdf8d108b4331`
- **MD5:** `f96372b5508c9f53a6451cec3850d662`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.17 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.2; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | cf94ecc0c4b72d8dd7853d3d8a6c5157127528c408ac9be8b8d51d559ea33970 | static_analysis |
| ip | 78.85.15.XXX | artifact_source |

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
