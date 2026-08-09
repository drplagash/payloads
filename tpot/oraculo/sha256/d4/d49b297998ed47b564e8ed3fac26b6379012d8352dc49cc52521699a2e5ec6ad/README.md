# 🧬 Payload Analysis

`d49b297998ed47b564e8ed3fac26b6379012d8352dc49cc52521699a2e5ec6ad`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:47:25.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d49b297998ed47b564e8ed3fac26b6379012d8352dc49cc52521699a2e5ec6ad`
- **SHA1:** `0e7e41ec27db0eaf47399ddf4127dc3858d4e951`
- **MD5:** `564fdeac91bb791c827a0ec1cf5ac244`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Public Key Version 2, Created Sun Sep 24 11:32:19 2028, Unknown Algorithm (0xc6) |
| Tamaño | 1.4 KiB |
| Entropía | 7.89 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Public Key Version 2, Created Sun Sep 24 11:32:19 2028, Unknown Algorithm (0xc6); high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d49b297998ed47b564e8ed3fac26b6379012d8352dc49cc52521699a2e5ec6ad | static_analysis |
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
