# 🧬 Payload Analysis

`47768b5e4980297a8022b5ffdf7c046607f94b8d5e28dc27a6a6afa5bd3bf70f`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Alta entropía / posible empaquetado o cifrado. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `47768b5e4980297a8022b5ffdf7c046607f94b8d5e28dc27a6a6afa5bd3bf70f`
- **MD5:** `f0832018b853ee29a98e083ff8d6fc15`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.48 |
| Strings | 32 |

## 🧠 Comportamiento observado

1. **Alta entropía / posible empaquetado o cifrado**

## 🔬 Evidencia de clasificación

- High entropy (7.5) — posible packer/encrypted

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://crl[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q4.crl0 | strings |
| url | hxxp://crl[.]globalsign[.]com/root-r3.crl0! | strings |
| url | hxxp://ocsp[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q40J | strings |
| url | hxxp://ocsp2[.]globalsign[.]com/rootr30; | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/gsatlasr3dvtlsca2025q4.crt0 | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/root-r3.crt06 | strings |
| url | hxxps://www[.]globalsign[.]com/repository/0 | strings |
| hash | 47768b5e4980297a8022b5ffdf7c046607f94b8d5e28dc27a6a6afa5bd3bf70f | static_analysis |
| ip | 151.101.194.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
