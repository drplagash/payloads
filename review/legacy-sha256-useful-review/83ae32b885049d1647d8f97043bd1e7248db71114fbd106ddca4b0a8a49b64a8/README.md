# 🧬 Payload Analysis

`83ae32b885049d1647d8f97043bd1e7248db71114fbd106ddca4b0a8a49b64a8`

## 📌 Resumen

Artefacto de 1.4 KiB. Entropía registrada: 7.03. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `83ae32b885049d1647d8f97043bd1e7248db71114fbd106ddca4b0a8a49b64a8`
- **SHA1:** `cc5de8a75ab70d0a9f249de4db30b990f2c69073`
- **MD5:** `65112bb3fabcc9dfec99cb895bb13024`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.03 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 83ae32b885049d1647d8f97043bd1e7248db71114fbd106ddca4b0a8a49b64a8 | static_analysis |
| ip | 186.132.11.XXX | artifact_source |

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
