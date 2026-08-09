# 🧬 Payload Analysis

`20552808eed2921ca176469659d91864c3888a1c3d8eaa73c7912c6325429ad3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `20552808eed2921ca176469659d91864c3888a1c3d8eaa73c7912c6325429ad3`
- **MD5:** `6e723811954f4409147ba729501a7b37`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | i386 COFF object |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=i386 COFF object; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 20552808eed2921ca176469659d91864c3888a1c3d8eaa73c7912c6325429ad3 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
