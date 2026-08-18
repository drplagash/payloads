# 🧬 Payload Analysis

`2c1009ae05e5a734ed6f323e5c58a7bcbe603192dfb5904169bb7e4630bed00d`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como compacted data. Presenta entropía elevada (7.86), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2c1009ae05e5a734ed6f323e5c58a7bcbe603192dfb5904169bb7e4630bed00d`
- **SHA1:** `235cfd3e5ab1403adb0a985ba3be592083a8e1e8`
- **MD5:** `cb205476aff731a256cff389f4fea3ef`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | compacted data |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=compacted data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 2c1009ae05e5a734ed6f323e5c58a7bcbe603192dfb5904169bb7e4630bed00d | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

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
