# 🧬 Payload Analysis

`91c0108c7164c2c1d517060e274318708dc961f4964cd3e3781bcd4a233684ff`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:47:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `91c0108c7164c2c1d517060e274318708dc961f4964cd3e3781bcd4a233684ff`
- **SHA1:** `7d90fa19be4a673fa5e91a14775ff7bc21156ed3`
- **MD5:** `cbdfdc5ff2ce75bc56bdd6d7e38d5e64`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ALAN game data version 2.6-65 |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ALAN game data version 2.6-65; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 91c0108c7164c2c1d517060e274318708dc961f4964cd3e3781bcd4a233684ff | static_analysis |
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
