# 🧬 Payload Analysis

`89e4e3630e9080adc07b3e50d059f3ee558702e2b9a4a19f4efe06afee414d5a`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/89e4e3630e9080adc07b3e50d059f3ee558702e2b9a4a19f4efe06afee414d5a.md](../../../../../malware-like/oraculo/botnet/89e4e3630e9080adc07b3e50d059f3ee558702e2b9a4a19f4efe06afee414d5a.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:38:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `89e4e3630e9080adc07b3e50d059f3ee558702e2b9a4a19f4efe06afee414d5a`
- **SHA1:** `f54c168fd222e06b0ff0ef1707edd6ae0b9f2f8a`
- **MD5:** `a5bcb4fc8736d87c2bddc383937d151a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 89e4e3630e9080adc07b3e50d059f3ee558702e2b9a4a19f4efe06afee414d5a | static_analysis |
| ip | 14.160.50.XXX | artifact_source |

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
