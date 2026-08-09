# 🧬 Payload Analysis

`fe0868397771a5548e5a0a092ab8cbd9ee4ef996ce70b14a1ef994269a0d8e73`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:42:32+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fe0868397771a5548e5a0a092ab8cbd9ee4ef996ce70b14a1ef994269a0d8e73`
- **SHA1:** `a44c25d84bfc7f1fd18be5443140857cd45c67ee`
- **MD5:** `9870b28e99573e809989bd58613d25b0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | SVr2 curses screen image, little-endian |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=SVr2 curses screen image, little-endian; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | fe0868397771a5548e5a0a092ab8cbd9ee4ef996ce70b14a1ef994269a0d8e73 | static_analysis |
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
