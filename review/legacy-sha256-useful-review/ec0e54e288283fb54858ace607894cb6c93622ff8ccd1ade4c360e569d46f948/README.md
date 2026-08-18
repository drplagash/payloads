# 🧬 Payload Analysis

`ec0e54e288283fb54858ace607894cb6c93622ff8ccd1ade4c360e569d46f948`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/ec0e54e288283fb54858ace607894cb6c93622ff8ccd1ade4c360e569d46f948.md](../../../../../malware-like/oraculo/botnet/ec0e54e288283fb54858ace607894cb6c93622ff8ccd1ade4c360e569d46f948.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:12:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ec0e54e288283fb54858ace607894cb6c93622ff8ccd1ade4c360e569d46f948`
- **SHA1:** `de0edab73d0f445c410c4af171146b87a39ba4a4`
- **MD5:** `16f28615272e4b0ba20df7993b77fcf3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | ec0e54e288283fb54858ace607894cb6c93622ff8ccd1ade4c360e569d46f948 | static_analysis |
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
