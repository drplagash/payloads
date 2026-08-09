# 🧬 Payload Analysis

`506ffa53ed1901d7051de77d6e4a82c6b8870893838bfafc8079453a168bf4e7`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `506ffa53ed1901d7051de77d6e4a82c6b8870893838bfafc8079453a168bf4e7`
- **SHA1:** `40b18f43d80a68f4c98baaa857f913f19a31fa2d`
- **MD5:** `2599c45e796446a0739677d140be094a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | SVr4 curses screen image, little-endian |
| Tamaño | 1.4 KiB |
| Entropía | 7.89 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=SVr4 curses screen image, little-endian; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 506ffa53ed1901d7051de77d6e4a82c6b8870893838bfafc8079453a168bf4e7 | static_analysis |
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
