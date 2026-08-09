# 🧬 Payload Analysis

`ddaa21c24bff845dd50105cccbd7d829f662a56c9c66d5c64539def878fb565c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Yara signature match. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:20+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ddaa21c24bff845dd50105cccbd7d829f662a56c9c66d5c64539def878fb565c`
- **MD5:** `1f9f18b8cdcf766570422c3f8c4fc6a5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.34 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Yara signature match**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; yara_matches=1; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | ddaa21c24bff845dd50105cccbd7d829f662a56c9c66d5c64539def878fb565c | static_analysis |
| ip | 174.7.32.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
