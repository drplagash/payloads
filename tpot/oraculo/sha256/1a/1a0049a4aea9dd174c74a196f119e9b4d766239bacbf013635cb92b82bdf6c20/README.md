# 🧬 Payload Analysis

`1a0049a4aea9dd174c74a196f119e9b4d766239bacbf013635cb92b82bdf6c20`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:31:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1a0049a4aea9dd174c74a196f119e9b4d766239bacbf013635cb92b82bdf6c20`
- **SHA1:** `220672192c5f12bef4f135c7715b69932aac2fea`
- **MD5:** `62904e771d1385c4c94f212d26eb1b25`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | SYMMETRY i386 executable (invalid @ 0) not stripped |
| Tamaño | 1.4 KiB |
| Entropía | 7.89 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=SYMMETRY i386 executable (invalid @ 0) not stripped; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 1a0049a4aea9dd174c74a196f119e9b4d766239bacbf013635cb92b82bdf6c20 | static_analysis |
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
