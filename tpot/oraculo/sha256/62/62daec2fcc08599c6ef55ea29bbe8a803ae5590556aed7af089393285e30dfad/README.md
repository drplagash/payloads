# 🧬 Payload Analysis

`62daec2fcc08599c6ef55ea29bbe8a803ae5590556aed7af089393285e30dfad`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:56+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `62daec2fcc08599c6ef55ea29bbe8a803ae5590556aed7af089393285e30dfad`
- **SHA1:** `fa8d4ad96e018921b531c89db45b537519d898d6`
- **MD5:** `255d2e57ac61d6afc484acaccf700dc8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 320 B |
| Entropía | 7.32 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.3; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 62daec2fcc08599c6ef55ea29bbe8a803ae5590556aed7af089393285e30dfad | static_analysis |
| ip | 213.209.159.XXX | artifact_source |

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
