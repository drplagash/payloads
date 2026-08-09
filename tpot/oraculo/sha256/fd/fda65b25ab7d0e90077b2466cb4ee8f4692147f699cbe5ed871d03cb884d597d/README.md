# 🧬 Payload Analysis

`fda65b25ab7d0e90077b2466cb4ee8f4692147f699cbe5ed871d03cb884d597d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fda65b25ab7d0e90077b2466cb4ee8f4692147f699cbe5ed871d03cb884d597d`
- **SHA1:** `6e856553d17b537c00764d096d7967f9f42823c3`
- **MD5:** `70d0fde8bf2d556faa6ca37888be4363`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xb8dd3459 689e521d |
| Tamaño | 1.4 KiB |
| Entropía | 7.89 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xb8dd3459 689e521d; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | fda65b25ab7d0e90077b2466cb4ee8f4692147f699cbe5ed871d03cb884d597d | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
