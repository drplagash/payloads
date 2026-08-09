# 🧬 Payload Analysis

`1224bc29497548dae0137c3dc3592b4d3e1741b158166599eaeed239a579928a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:48:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1224bc29497548dae0137c3dc3592b4d3e1741b158166599eaeed239a579928a`
- **SHA1:** `89495f83f9bd8f06653d92fe1684ae2bfb534a22`
- **MD5:** `75e2f2a1e8b70b8cc9f92a68c91f010d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 398 B |
| Entropía | 5.38 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 103.123.226.XXX | static_analysis |
| ip | 190.179.144.XXX | static_analysis |
| hash | 1224bc29497548dae0137c3dc3592b4d3e1741b158166599eaeed239a579928a | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
