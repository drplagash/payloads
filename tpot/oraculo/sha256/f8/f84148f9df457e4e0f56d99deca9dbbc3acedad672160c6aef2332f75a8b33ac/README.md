# 🧬 Payload Analysis

`f84148f9df457e4e0f56d99deca9dbbc3acedad672160c6aef2332f75a8b33ac`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f84148f9df457e4e0f56d99deca9dbbc3acedad672160c6aef2332f75a8b33ac`
- **MD5:** `13976090f360a9c07deab0f94ef2ca4f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | apollo a88k COFF executable not stripped - version 25818 |
| Tamaño | 1.4 KiB |
| Entropía | 7.85 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=apollo a88k COFF executable not stripped - version 25818; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | f84148f9df457e4e0f56d99deca9dbbc3acedad672160c6aef2332f75a8b33ac | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
