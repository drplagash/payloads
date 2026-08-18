# 🧬 Payload Analysis

`d0ffa99ea12f07222f890f495d0af02d0e114840358f4e2978f31cd22b26c6ef`

## 📌 Resumen

Artefacto de 1.4 KiB. Presenta entropía elevada (7.80), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:54:30.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d0ffa99ea12f07222f890f495d0af02d0e114840358f4e2978f31cd22b26c6ef`
- **SHA1:** `0667de7e7c90f5253ea26bc2ba31feb0ce87ead5`
- **MD5:** `e706c7fa22ca9035e4fb932b7b56cd7a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.8 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d0ffa99ea12f07222f890f495d0af02d0e114840358f4e2978f31cd22b26c6ef | static_analysis |
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
