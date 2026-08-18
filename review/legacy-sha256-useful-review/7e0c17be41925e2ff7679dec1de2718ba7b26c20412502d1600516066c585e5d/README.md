# 🧬 Payload Analysis

`7e0c17be41925e2ff7679dec1de2718ba7b26c20412502d1600516066c585e5d`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/7e0c17be41925e2ff7679dec1de2718ba7b26c20412502d1600516066c585e5d.md](../../../../../malware-like/oraculo/botnet/7e0c17be41925e2ff7679dec1de2718ba7b26c20412502d1600516066c585e5d.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:47:25.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7e0c17be41925e2ff7679dec1de2718ba7b26c20412502d1600516066c585e5d`
- **SHA1:** `8276621e5378a70ce6d17203f573afcd0ea94b85`
- **MD5:** `edc293fa6a2acc35c7e026aadc8c5772`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.83 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 7e0c17be41925e2ff7679dec1de2718ba7b26c20412502d1600516066c585e5d | static_analysis |
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
