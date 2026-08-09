# 🧬 Payload Analysis

`deda424a6f502babf12570d8f5c212b8af27c429b90c198fa61532b686a84af1`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:13:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `deda424a6f502babf12570d8f5c212b8af27c429b90c198fa61532b686a84af1`
- **SHA1:** `5f5afd62f417a5490b84905f69b928a5a44578a9`
- **MD5:** `b4cfbb6898d23ad1e7d216926fe6d70a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xeb41635d 138a43f3 |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xeb41635d 138a43f3; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | deda424a6f502babf12570d8f5c212b8af27c429b90c198fa61532b686a84af1 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
