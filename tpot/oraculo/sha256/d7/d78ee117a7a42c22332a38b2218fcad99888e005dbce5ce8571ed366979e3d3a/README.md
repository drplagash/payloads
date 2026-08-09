# 🧬 Payload Analysis

`d78ee117a7a42c22332a38b2218fcad99888e005dbce5ce8571ed366979e3d3a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d78ee117a7a42c22332a38b2218fcad99888e005dbce5ce8571ed366979e3d3a`
- **SHA1:** `c0cc29526c61d76c606317b0f04d114e7731a1ea`
- **MD5:** `89bc023ebc8cd236b17e5a9bfd0a5500`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d78ee117a7a42c22332a38b2218fcad99888e005dbce5ce8571ed366979e3d3a | static_analysis |
| ip | 101.50.75.XXX | artifact_source |

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
