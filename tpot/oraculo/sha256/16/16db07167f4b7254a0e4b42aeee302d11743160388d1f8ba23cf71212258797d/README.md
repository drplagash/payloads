# 🧬 Payload Analysis

`16db07167f4b7254a0e4b42aeee302d11743160388d1f8ba23cf71212258797d`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `16db07167f4b7254a0e4b42aeee302d11743160388d1f8ba23cf71212258797d`
- **SHA1:** `cd0e1416af7d9cd17a6215b7a2c89e80f901b6da`
- **MD5:** `f95a858e19ca3fe3eddf57c5a77dceb2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Public Key |
| Tamaño | 1.4 KiB |
| Entropía | 7.85 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Public Key; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 16db07167f4b7254a0e4b42aeee302d11743160388d1f8ba23cf71212258797d | static_analysis |
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
