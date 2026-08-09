# 🧬 Payload Analysis

`ef910d0ae951788cdb16fc5b46e5052fd6ef9dad83e75b2065b82220cf953a34`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ef910d0ae951788cdb16fc5b46e5052fd6ef9dad83e75b2065b82220cf953a34`
- **SHA1:** `8c214c06aac554ea5e62bdf3895250e27188ce78`
- **MD5:** `8182558e3a9a4a683e2f6cde411fc434`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.48 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 13.89.100.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | ef910d0ae951788cdb16fc5b46e5052fd6ef9dad83e75b2065b82220cf953a34 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
