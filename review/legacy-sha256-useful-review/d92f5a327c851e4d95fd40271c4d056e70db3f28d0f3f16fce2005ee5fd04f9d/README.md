# 🧬 Payload Analysis

`d92f5a327c851e4d95fd40271c4d056e70db3f28d0f3f16fce2005ee5fd04f9d`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/d92f5a327c851e4d95fd40271c4d056e70db3f28d0f3f16fce2005ee5fd04f9d.md](../../../../../malware-like/oraculo/botnet/d92f5a327c851e4d95fd40271c4d056e70db3f28d0f3f16fce2005ee5fd04f9d.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:52:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d92f5a327c851e4d95fd40271c4d056e70db3f28d0f3f16fce2005ee5fd04f9d`
- **SHA1:** `6a93cd1c8f76071d1cb25bed6e1a578eb1e8dba9`
- **MD5:** `1a86ec447d36f92e05a1fd74d1c61435`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.91 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d92f5a327c851e4d95fd40271c4d056e70db3f28d0f3f16fce2005ee5fd04f9d | static_analysis |
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
