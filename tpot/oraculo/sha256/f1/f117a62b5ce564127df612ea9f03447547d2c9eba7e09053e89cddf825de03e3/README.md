# 🧬 Payload Analysis

`f117a62b5ce564127df612ea9f03447547d2c9eba7e09053e89cddf825de03e3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:02:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f117a62b5ce564127df612ea9f03447547d2c9eba7e09053e89cddf825de03e3`
- **SHA1:** `5a85c63eb93591b0f8d33dba9a60711c4daf679e`
- **MD5:** `31ede9b9aacb10cf6683390432c7a631`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.93 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | f117a62b5ce564127df612ea9f03447547d2c9eba7e09053e89cddf825de03e3 | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

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
