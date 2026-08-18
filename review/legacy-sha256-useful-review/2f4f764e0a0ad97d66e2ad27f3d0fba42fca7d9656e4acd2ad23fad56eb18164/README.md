# 🧬 Payload Analysis

`2f4f764e0a0ad97d66e2ad27f3d0fba42fca7d9656e4acd2ad23fad56eb18164`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.06. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:52:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2f4f764e0a0ad97d66e2ad27f3d0fba42fca7d9656e4acd2ad23fad56eb18164`
- **SHA1:** `2f053c6d9658a2380f22b26d507827acd5ed04c0`
- **MD5:** `08e4fdd27b5c9eeab836e482c4ac80a3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.06 |
| Strings | 48 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.1; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 2f4f764e0a0ad97d66e2ad27f3d0fba42fca7d9656e4acd2ad23fad56eb18164 | static_analysis |
| ip | 128.70.137.XXX | artifact_source |

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
