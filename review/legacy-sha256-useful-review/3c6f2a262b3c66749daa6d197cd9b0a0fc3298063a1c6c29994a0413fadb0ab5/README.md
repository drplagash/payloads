# 🧬 Payload Analysis

`3c6f2a262b3c66749daa6d197cd9b0a0fc3298063a1c6c29994a0413fadb0ab5`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3c6f2a262b3c66749daa6d197cd9b0a0fc3298063a1c6c29994a0413fadb0ab5`
- **SHA1:** `a66c680995264b9e99cd4482ee0cd7d4dfd9ded9`
- **MD5:** `10d977c049b638ecbbd83f8cabd493d4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Public Key Version 7 |
| Tamaño | 1.4 KiB |
| Entropía | 7.89 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Public Key Version 7; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 3c6f2a262b3c66749daa6d197cd9b0a0fc3298063a1c6c29994a0413fadb0ab5 | static_analysis |
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
