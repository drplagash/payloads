# 🧬 Payload Analysis

`6e588cc2266e08de68154883949e0ea2e5f5ddd1cdefcb2ca0228b7405510a1c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:20+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6e588cc2266e08de68154883949e0ea2e5f5ddd1cdefcb2ca0228b7405510a1c`
- **MD5:** `ae128bd958e0ed2364bb96bb32e4d139`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XENIX 8086 relocatable or i286 small model |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=XENIX 8086 relocatable or i286 small model; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 6e588cc2266e08de68154883949e0ea2e5f5ddd1cdefcb2ca0228b7405510a1c | static_analysis |
| ip | 103.207.52.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
