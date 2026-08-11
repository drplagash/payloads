# 🧬 Payload Analysis

`fa0e82e0153abd23a0d8bc482bb2ebc0eae84122488abb73d85884b284a302cb`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Alta entropía / posible empaquetado o cifrado. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/fa0e82e0153abd23a0d8bc482bb2ebc0eae84122488abb73d85884b284a302cb.md](../../../../../malware-like/oraculo/botnet/fa0e82e0153abd23a0d8bc482bb2ebc0eae84122488abb73d85884b284a302cb.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:05:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fa0e82e0153abd23a0d8bc482bb2ebc0eae84122488abb73d85884b284a302cb`
- **SHA1:** `46ddf6c71b04a87434ff6c1ec67d7ea6ac14f60f`
- **MD5:** `f26357afb3f0d6da458f3f9b79078689`

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
Mirai-like indicators in strings; High entropy (8.0) — posible packer/encrypted
Mirai-like indicators in strings; High entropy (8.0) — posible packer/encrypted
- Motivos técnicos: mime=data; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | fa0e82e0153abd23a0d8bc482bb2ebc0eae84122488abb73d85884b284a302cb | static_analysis |
| ip | 176.237.208.XXX | artifact_source |

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
