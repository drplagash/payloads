# 🧬 Payload Analysis

`c50f7d21d211d4ab832d5e290e337e0851d16c05e243eae458cfcdf33a30ca59`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:26:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c50f7d21d211d4ab832d5e290e337e0851d16c05e243eae458cfcdf33a30ca59`
- **SHA1:** `df94d7c7a763de322e312ba4eaee1412de55f08d`
- **MD5:** `5896f3a350abba68bdb87d4537c5909a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c50f7d21d211d4ab832d5e290e337e0851d16c05e243eae458cfcdf33a30ca59 | static_analysis |
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
