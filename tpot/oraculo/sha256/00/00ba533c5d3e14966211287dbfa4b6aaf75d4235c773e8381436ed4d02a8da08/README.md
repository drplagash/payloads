# 🧬 Payload Analysis

`00ba533c5d3e14966211287dbfa4b6aaf75d4235c773e8381436ed4d02a8da08`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:17:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `00ba533c5d3e14966211287dbfa4b6aaf75d4235c773e8381436ed4d02a8da08`
- **SHA1:** `0a4b7557caac56981d938141293d5c54cdd8a009`
- **MD5:** `307decb67e3bafa01dc66b40501fe43d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key Version 4, Created Thu Jun 23 00:52:37 2022, Unknown Algorithm (0x51) |
| Tamaño | 1.4 KiB |
| Entropía | 7.84 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key Version 4, Created Thu Jun 23 00:52:37 2022, Unknown Algorithm (0x51); high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 00ba533c5d3e14966211287dbfa4b6aaf75d4235c773e8381436ed4d02a8da08 | static_analysis |
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
