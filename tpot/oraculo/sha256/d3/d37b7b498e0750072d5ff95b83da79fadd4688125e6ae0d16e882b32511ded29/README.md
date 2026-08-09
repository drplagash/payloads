# 🧬 Payload Analysis

`d37b7b498e0750072d5ff95b83da79fadd4688125e6ae0d16e882b32511ded29`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d37b7b498e0750072d5ff95b83da79fadd4688125e6ae0d16e882b32511ded29`
- **SHA1:** `6a7accd534ae640b1d4e6558a71c9fe7d4470663`
- **MD5:** `0681a4cae17a8e797c6367c3f600f378`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.34 |
| Strings | 38 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 107.189.24.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | d37b7b498e0750072d5ff95b83da79fadd4688125e6ae0d16e882b32511ded29 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
