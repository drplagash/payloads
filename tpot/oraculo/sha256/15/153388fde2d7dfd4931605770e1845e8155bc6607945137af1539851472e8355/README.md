# 🧬 Payload Analysis

`153388fde2d7dfd4931605770e1845e8155bc6607945137af1539851472e8355`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `153388fde2d7dfd4931605770e1845e8155bc6607945137af1539851472e8355`
- **SHA1:** `5be41c47861e3e1724b4e403f7c26f0ad763c02f`
- **MD5:** `94d8f1c388bb8e55830ca390e0a42241`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | MPEG ADTS, layer I, v2, 256 kbps, 22.05 kHz, Stereo |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=MPEG ADTS, layer I, v2, 256 kbps, 22.05 kHz, Stereo; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 153388fde2d7dfd4931605770e1845e8155bc6607945137af1539851472e8355 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | media or resource |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
