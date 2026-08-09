# 🧬 Payload Analysis

`dc324f9c273b6cdebe5e72f92b0ee321acab10688bc85507f0603c51b7266c7a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:41:51+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dc324f9c273b6cdebe5e72f92b0ee321acab10688bc85507f0603c51b7266c7a`
- **SHA1:** `752335eaee68602c4273a14ebbde62eb416d4fd5`
- **MD5:** `759b78c51724eee359ef23396e1c5943`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 410 B |
| Entropía | 5.37 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 172.110.223.XXX | static_analysis |
| ip | 190.179.166.XXX | static_analysis |
| hash | dc324f9c273b6cdebe5e72f92b0ee321acab10688bc85507f0603c51b7266c7a | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
