# 🧬 Payload Analysis

`936cc36522e8873168d1716b9fbfc68193054f3e9a91dd5cf29471dc3af7c9fa`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: High entropy obfuscation, Binary execution. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `936cc36522e8873168d1716b9fbfc68193054f3e9a91dd5cf29471dc3af7c9fa`
- **SHA1:** `6ec92ef801b1927fe2ac7c3bfbb638ab048a9b1f`
- **MD5:** `ca8b0d052790eb428ed5abcbf7a9841a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | SVR2 pure executable (Amdahl-UTS) not stripped |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **High entropy obfuscation**
2. **Binary execution**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=SVR2 pure executable (Amdahl-UTS) not stripped; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 936cc36522e8873168d1716b9fbfc68193054f3e9a91dd5cf29471dc3af7c9fa | static_analysis |
| ip | 2.135.242.XXX | artifact_source |

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
