# 🧬 Payload Analysis

`2dcbead4e30ba27e02b6a4433436d51d01a7464021218942a1a0e97d49d7dc68`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:26:56+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2dcbead4e30ba27e02b6a4433436d51d01a7464021218942a1a0e97d49d7dc68`
- **SHA1:** `156881b2ea53881074775cddc2303692eed768a4`
- **MD5:** `5291e869498ed7938d17b64f17984d79`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Public Key |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Public Key; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 2dcbead4e30ba27e02b6a4433436d51d01a7464021218942a1a0e97d49d7dc68 | static_analysis |
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
