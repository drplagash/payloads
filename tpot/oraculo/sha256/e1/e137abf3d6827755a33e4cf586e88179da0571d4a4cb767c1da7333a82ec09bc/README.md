# 🧬 Payload Analysis

`e137abf3d6827755a33e4cf586e88179da0571d4a4cb767c1da7333a82ec09bc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:26:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e137abf3d6827755a33e4cf586e88179da0571d4a4cb767c1da7333a82ec09bc`
- **SHA1:** `9d114213feb47376d43fba1a5de9deee0d3354a7`
- **MD5:** `eef747d071fcbdd6311703b1f01ba4a7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | MPEG ADTS, layer III,  v2.5, 160 kbps, 12 kHz, 2x Monaural |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=MPEG ADTS, layer III,  v2.5, 160 kbps, 12 kHz, 2x Monaural; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | e137abf3d6827755a33e4cf586e88179da0571d4a4cb767c1da7333a82ec09bc | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

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
