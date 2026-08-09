# 🧬 Payload Analysis

`fdacbf226b5ff496c80386960d297fe44218ed3e65030219f0b6e8f3b55cf2bc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: High entropy. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:09:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fdacbf226b5ff496c80386960d297fe44218ed3e65030219f0b6e8f3b55cf2bc`
- **SHA1:** `99ccb9b2243a3702e8fd693ec4a7b7d35cd78ffb`
- **MD5:** `37f828f7cd010a8afc2fb217d9a77fe0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0x8c935a6e a3583597 |
| Tamaño | 1.4 KiB |
| Entropía | 7.84 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **High entropy**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0x8c935a6e a3583597; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | fdacbf226b5ff496c80386960d297fe44218ed3e65030219f0b6e8f3b55cf2bc | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
