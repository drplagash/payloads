# 🧬 Payload Analysis

`ac1b6ca68105abb6f5488ad0f5e238e00af30f5d6986bdcf960203bb07a5ac44`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/ac1b6ca68105abb6f5488ad0f5e238e00af30f5d6986bdcf960203bb07a5ac44.md](../../../../../malware-like/oraculo/botnet/ac1b6ca68105abb6f5488ad0f5e238e00af30f5d6986bdcf960203bb07a5ac44.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ac1b6ca68105abb6f5488ad0f5e238e00af30f5d6986bdcf960203bb07a5ac44`
- **SHA1:** `39e51637453af4597f397deea7940b1bbeb353cf`
- **MD5:** `c2f937765a9ea10ab35fbf09608662f7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | ac1b6ca68105abb6f5488ad0f5e238e00af30f5d6986bdcf960203bb07a5ac44 | static_analysis |
| ip | 2.184.239.XXX | artifact_source |

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
