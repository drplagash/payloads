# 🧬 Payload Analysis

`e45412b2a5eb8c4a81dc6fb50b29cd30178006200935157b9c9a18e00294f474`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e45412b2a5eb8c4a81dc6fb50b29cd30178006200935157b9c9a18e00294f474`
- **SHA1:** `44e9c0762089bbbad4cccda1e0f4719fffe0d4f0`
- **MD5:** `286e453c40d9e1ed17d53e4154d3d15b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | IRIS Showcase template - version -48 |
| Tamaño | 1.4 KiB |
| Entropía | 7.84 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=IRIS Showcase template - version -48; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | e45412b2a5eb8c4a81dc6fb50b29cd30178006200935157b9c9a18e00294f474 | static_analysis |
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
