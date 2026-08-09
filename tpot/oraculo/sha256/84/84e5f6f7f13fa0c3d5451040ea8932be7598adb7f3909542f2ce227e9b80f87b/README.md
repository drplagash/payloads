# 🧬 Payload Analysis

`84e5f6f7f13fa0c3d5451040ea8932be7598adb7f3909542f2ce227e9b80f87b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Alta entropía / posible empaquetado o cifrado. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:05+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `84e5f6f7f13fa0c3d5451040ea8932be7598adb7f3909542f2ce227e9b80f87b`
- **SHA1:** `9f60a51a967d5a81e6ecf6eecf72b96a8eb092a6`
- **MD5:** `a9ea0278b032fdf183f4d40ac46fb00e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.81 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Alta entropía / posible empaquetado o cifrado**

## 🔬 Evidencia de clasificación

- High entropy (7.8) — posible packer/encrypted
- Motivos técnicos: mime=data; high_entropy=7.8; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 84e5f6f7f13fa0c3d5451040ea8932be7598adb7f3909542f2ce227e9b80f87b | static_analysis |
| ip | 78.172.197.XXX | artifact_source |

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
