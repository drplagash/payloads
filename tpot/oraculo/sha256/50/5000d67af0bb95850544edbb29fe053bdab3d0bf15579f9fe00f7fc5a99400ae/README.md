# 🧬 Payload Analysis

`5000d67af0bb95850544edbb29fe053bdab3d0bf15579f9fe00f7fc5a99400ae`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/5000d67af0bb95850544edbb29fe053bdab3d0bf15579f9fe00f7fc5a99400ae.md](../../../../../malware-like/oraculo/botnet/5000d67af0bb95850544edbb29fe053bdab3d0bf15579f9fe00f7fc5a99400ae.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5000d67af0bb95850544edbb29fe053bdab3d0bf15579f9fe00f7fc5a99400ae`
- **SHA1:** `2c93a975f669026b0cd6a770830cd7faf0762347`
- **MD5:** `510f4ca8068cf08fbb0ae5a77f7d86cc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.89 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 5000d67af0bb95850544edbb29fe053bdab3d0bf15579f9fe00f7fc5a99400ae | static_analysis |
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
