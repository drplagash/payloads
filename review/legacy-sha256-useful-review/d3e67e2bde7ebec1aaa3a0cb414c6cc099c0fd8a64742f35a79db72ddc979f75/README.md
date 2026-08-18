# 🧬 Payload Analysis

`d3e67e2bde7ebec1aaa3a0cb414c6cc099c0fd8a64742f35a79db72ddc979f75`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/d3e67e2bde7ebec1aaa3a0cb414c6cc099c0fd8a64742f35a79db72ddc979f75.md](../../../../../malware-like/oraculo/botnet/d3e67e2bde7ebec1aaa3a0cb414c6cc099c0fd8a64742f35a79db72ddc979f75.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:03:26.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d3e67e2bde7ebec1aaa3a0cb414c6cc099c0fd8a64742f35a79db72ddc979f75`
- **SHA1:** `9e753505f76993dde033113f6c3c8d933936952b`
- **MD5:** `d438143e57767e7f104472b7fad09e8e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d3e67e2bde7ebec1aaa3a0cb414c6cc099c0fd8a64742f35a79db72ddc979f75 | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

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
