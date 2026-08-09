# 🧬 Payload Analysis

`de1ace98daf6eccc87eea99b23d2266c9e197ff22700d83bbe45e53d4e2ccde7`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `de1ace98daf6eccc87eea99b23d2266c9e197ff22700d83bbe45e53d4e2ccde7`
- **SHA1:** `dc954a5c4c1d74f50b043e750738834ab4e5d2d0`
- **MD5:** `bc7ad00d191427c63173e53e6322ef8f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Berkeley vfont data |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Berkeley vfont data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | de1ace98daf6eccc87eea99b23d2266c9e197ff22700d83bbe45e53d4e2ccde7 | static_analysis |
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
