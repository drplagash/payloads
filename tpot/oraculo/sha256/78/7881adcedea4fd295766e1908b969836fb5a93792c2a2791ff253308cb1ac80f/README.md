# 🧬 Payload Analysis

`7881adcedea4fd295766e1908b969836fb5a93792c2a2791ff253308cb1ac80f`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:09:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7881adcedea4fd295766e1908b969836fb5a93792c2a2791ff253308cb1ac80f`
- **SHA1:** `26449f4719aa462a4a00af16240772d3d5470f0d`
- **MD5:** `96e872cf160c49cf3d59b4d713b87a84`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 410 B |
| Entropía | 5.36 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 172.110.223.XXX | static_analysis |
| ip | 190.179.166.XXX | static_analysis |
| hash | 7881adcedea4fd295766e1908b969836fb5a93792c2a2791ff253308cb1ac80f | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
