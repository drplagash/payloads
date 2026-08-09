# 🧬 Payload Analysis

`d2c2bc6a2bd318fcd553c6d899dd5037c262c036cdb6494f67b3d449c5fe8020`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Alta entropía / posible empaquetado o cifrado. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:33:28.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d2c2bc6a2bd318fcd553c6d899dd5037c262c036cdb6494f67b3d449c5fe8020`
- **MD5:** `72961f25632dac73618bf22686f85d5f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Alta entropía / posible empaquetado o cifrado**

## 🔬 Evidencia de clasificación

- Mirai-like indicators in strings; High entropy (8.0) — posible packer/encrypted
- Motivos técnicos: mime=data; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d2c2bc6a2bd318fcd553c6d899dd5037c262c036cdb6494f67b3d449c5fe8020 | static_analysis |
| ip | 213.157.51.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
