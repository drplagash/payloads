# 🧬 Payload Analysis

`66590e2c9379e9d7fee9eaecd8e37399419df32a1de458c900544f129c04a26a`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:46:01.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `66590e2c9379e9d7fee9eaecd8e37399419df32a1de458c900544f129c04a26a`
- **SHA1:** `1c07bc7ac37579a25f101049a504e19c929f8ba7`
- **MD5:** `5e60368702c346511ca44ef7e43b08b0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Dyalog APL version -75.-24 |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Dyalog APL version -75.-24; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 66590e2c9379e9d7fee9eaecd8e37399419df32a1de458c900544f129c04a26a | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

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
