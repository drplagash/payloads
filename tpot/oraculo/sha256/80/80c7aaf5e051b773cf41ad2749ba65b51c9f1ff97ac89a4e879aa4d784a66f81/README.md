# 🧬 Payload Analysis

`80c7aaf5e051b773cf41ad2749ba65b51c9f1ff97ac89a4e879aa4d784a66f81`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:59+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `80c7aaf5e051b773cf41ad2749ba65b51c9f1ff97ac89a4e879aa4d784a66f81`
- **SHA1:** `28c11780ad4aa6a324ca182e5f8d78b5854a4ec2`
- **MD5:** `05fad8ebd0726925c121678851c24844`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, Unicode text, UTF-8 text, with very long lines (1059), with CRLF, LF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.38 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=HTML document, Unicode text, UTF-8 text, with very long lines (1059), with CRLF, LF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 80c7aaf5e051b773cf41ad2749ba65b51c9f1ff97ac89a4e879aa4d784a66f81 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
