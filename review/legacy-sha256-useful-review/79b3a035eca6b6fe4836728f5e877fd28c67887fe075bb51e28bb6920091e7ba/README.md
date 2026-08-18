# 🧬 Payload Analysis

`79b3a035eca6b6fe4836728f5e877fd28c67887fe075bb51e28bb6920091e7ba`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/79b3a035eca6b6fe4836728f5e877fd28c67887fe075bb51e28bb6920091e7ba.md](../../../../../malware-like/oraculo/botnet/79b3a035eca6b6fe4836728f5e877fd28c67887fe075bb51e28bb6920091e7ba.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `79b3a035eca6b6fe4836728f5e877fd28c67887fe075bb51e28bb6920091e7ba`
- **SHA1:** `f054c2a938f138150e739495a198614eab939c7a`
- **MD5:** `ba749a0065709ac28657f90d8fa332fc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 79b3a035eca6b6fe4836728f5e877fd28c67887fe075bb51e28bb6920091e7ba | static_analysis |
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
