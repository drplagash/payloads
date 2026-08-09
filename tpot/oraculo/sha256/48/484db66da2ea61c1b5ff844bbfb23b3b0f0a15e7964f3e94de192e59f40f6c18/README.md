# 🧬 Payload Analysis

`484db66da2ea61c1b5ff844bbfb23b3b0f0a15e7964f3e94de192e59f40f6c18`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.14. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `484db66da2ea61c1b5ff844bbfb23b3b0f0a15e7964f3e94de192e59f40f6c18`
- **SHA1:** `159fdfa5e2f04b5dfbee0745e06a3908dd779980`
- **MD5:** `fe0e05c8eb6ac4cf2d7c329b2ed7d9b9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.14 |
| Strings | 26 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.1; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 484db66da2ea61c1b5ff844bbfb23b3b0f0a15e7964f3e94de192e59f40f6c18 | static_analysis |
| ip | 85.237.63.XXX | artifact_source |

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
