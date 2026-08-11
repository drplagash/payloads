# 🧬 Payload Analysis

`19c3a286aaa5d390dce39a734184c3a3e506ec3feb9d9d33dc7f8323827cf594`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/19c3a286aaa5d390dce39a734184c3a3e506ec3feb9d9d33dc7f8323827cf594.md](../../../../../malware-like/oraculo/botnet/19c3a286aaa5d390dce39a734184c3a3e506ec3feb9d9d33dc7f8323827cf594.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `19c3a286aaa5d390dce39a734184c3a3e506ec3feb9d9d33dc7f8323827cf594`
- **SHA1:** `c918a18a889e626c742e9592a7b84a983e1d0899`
- **MD5:** `2eb6bab284493f215c55dc8eca0ab863`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Public Key |
| Tamaño | 4.0 KiB |
| Entropía | 7.82 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Public Key; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 19c3a286aaa5d390dce39a734184c3a3e506ec3feb9d9d33dc7f8323827cf594 | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
