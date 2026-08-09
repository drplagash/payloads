# 🧬 Payload Analysis

`a961b9123e2c9e27d9f16f514d0816047f51eb19c303f91a61d6c9a349492368`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:35+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a961b9123e2c9e27d9f16f514d0816047f51eb19c303f91a61d6c9a349492368`
- **SHA1:** `0bf73ef8accd30fea18444346d3e681990312d76`
- **MD5:** `211fa3db5cd2559e11f4cfb36f95c670`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 413 B |
| Entropía | 5.4 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| ip | 51.81.22.XXX | static_analysis |
| hash | a961b9123e2c9e27d9f16f514d0816047f51eb19c303f91a61d6c9a349492368 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
