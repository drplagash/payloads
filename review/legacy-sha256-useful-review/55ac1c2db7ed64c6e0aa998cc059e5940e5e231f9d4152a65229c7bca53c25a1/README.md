# 🧬 Payload Analysis

`55ac1c2db7ed64c6e0aa998cc059e5940e5e231f9d4152a65229c7bca53c25a1`

## 📌 Resumen

Artefacto de 1.4 KiB. Entropía registrada: 7.14. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:35:39.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `55ac1c2db7ed64c6e0aa998cc059e5940e5e231f9d4152a65229c7bca53c25a1`
- **SHA1:** `c1f23faaeee886c02d695858a5ba47bc69ece9e3`
- **MD5:** `2c6b84aa5af8a627011ddfa54eccb9e3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.14 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.1; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 55ac1c2db7ed64c6e0aa998cc059e5940e5e231f9d4152a65229c7bca53c25a1 | static_analysis |
| ip | 200.43.89.XXX | artifact_source |

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
