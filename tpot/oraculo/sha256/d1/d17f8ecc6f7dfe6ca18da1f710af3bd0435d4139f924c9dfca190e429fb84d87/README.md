# 🧬 Payload Analysis

`d17f8ecc6f7dfe6ca18da1f710af3bd0435d4139f924c9dfca190e429fb84d87`

## 📌 Resumen

Artefacto de 1.4 KiB. Entropía registrada: 7.16. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:52:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d17f8ecc6f7dfe6ca18da1f710af3bd0435d4139f924c9dfca190e429fb84d87`
- **SHA1:** `6d171de85178aee47d2bd5ac9fd42dceaf0757ec`
- **MD5:** `b3506c8049c5bf7e32e55aacc3152ef4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.16 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.2; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d17f8ecc6f7dfe6ca18da1f710af3bd0435d4139f924c9dfca190e429fb84d87 | static_analysis |
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
