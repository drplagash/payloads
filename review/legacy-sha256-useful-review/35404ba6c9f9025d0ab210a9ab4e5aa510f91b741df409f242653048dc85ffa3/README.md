# 🧬 Payload Analysis

`35404ba6c9f9025d0ab210a9ab4e5aa510f91b741df409f242653048dc85ffa3`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como DOS executable (COM), start instruction 0x8cbb4c67 6696df9f. Presenta entropía elevada (7.87), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `35404ba6c9f9025d0ab210a9ab4e5aa510f91b741df409f242653048dc85ffa3`
- **SHA1:** `3118b790d2c6acd80bc5dd802e095c8f158f58f6`
- **MD5:** `fa5df6800aecffcd2192bf5340f4e928`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0x8cbb4c67 6696df9f |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0x8cbb4c67 6696df9f; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 35404ba6c9f9025d0ab210a9ab4e5aa510f91b741df409f242653048dc85ffa3 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
