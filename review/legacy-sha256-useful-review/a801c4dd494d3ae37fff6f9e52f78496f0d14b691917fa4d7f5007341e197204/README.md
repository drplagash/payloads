# 🧬 Payload Analysis

`a801c4dd494d3ae37fff6f9e52f78496f0d14b691917fa4d7f5007341e197204`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:19.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a801c4dd494d3ae37fff6f9e52f78496f0d14b691917fa4d7f5007341e197204`
- **SHA1:** `7f4916d969e89bd397820ff264d3a3935b6dc6e6`
- **MD5:** `44c86364f83486129785c7566f057e11`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Public Key |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Public Key; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | a801c4dd494d3ae37fff6f9e52f78496f0d14b691917fa4d7f5007341e197204 | static_analysis |
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
