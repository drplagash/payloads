# 🧬 Payload Analysis

`c39c88776f79ff548fb99a44c4f39c7939261a04da728181e69327030f349080`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Alta entropía / posible empaquetado o cifrado. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c39c88776f79ff548fb99a44c4f39c7939261a04da728181e69327030f349080`
- **MD5:** `bbfde5d9909b09abc9b5c730b1c06cde`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.73 |
| Strings | 2 |

## 🧠 Comportamiento observado

1. **Alta entropía / posible empaquetado o cifrado**

## 🔬 Evidencia de clasificación

- Mirai-like indicators in strings; High entropy (7.7) — posible packer/encrypted
Mirai-like indicators in strings; High entropy (7.7) — posible packer/encrypted

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c39c88776f79ff548fb99a44c4f39c7939261a04da728181e69327030f349080 | static_analysis |
| ip | 45.82.78.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
