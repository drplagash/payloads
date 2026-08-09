# 🧬 Payload Analysis

`03058f4d0534c32af05d76597f7394c48766c8c2c0fdbd4df5f05834144dc502`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:09:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `03058f4d0534c32af05d76597f7394c48766c8c2c0fdbd4df5f05834144dc502`
- **SHA1:** `354ef09b9b6edff5194ca731340122d9cca62ed8`
- **MD5:** `e95795d8560924a2c36228e88ce94be4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | amd 29k coff prebar executable |
| Tamaño | 1.4 KiB |
| Entropía | 7.85 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=amd 29k coff prebar executable; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 03058f4d0534c32af05d76597f7394c48766c8c2c0fdbd4df5f05834144dc502 | static_analysis |
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
