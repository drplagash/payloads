# 🧬 Payload Analysis

`9cad0e30b9191e188d2492e74495fd2a3cefb32e5225cb9a333d891aa95e9672`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:32:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9cad0e30b9191e188d2492e74495fd2a3cefb32e5225cb9a333d891aa95e9672`
- **SHA1:** `9ebfbcf93d34871bbb97306385332a9d5158b8a8`
- **MD5:** `3f43dd302cf9db8d9df8629a7735693f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Dyalog APL external variable exclusive version -28.-101 |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Dyalog APL external variable exclusive version -28.-101; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 9cad0e30b9191e188d2492e74495fd2a3cefb32e5225cb9a333d891aa95e9672 | static_analysis |
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
