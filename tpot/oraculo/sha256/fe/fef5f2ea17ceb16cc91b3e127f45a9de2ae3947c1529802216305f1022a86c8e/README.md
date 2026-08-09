# 🧬 Payload Analysis

`fef5f2ea17ceb16cc91b3e127f45a9de2ae3947c1529802216305f1022a86c8e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fef5f2ea17ceb16cc91b3e127f45a9de2ae3947c1529802216305f1022a86c8e`
- **SHA1:** `9418c9a80b6a3512e60b7740015808df7823d150`
- **MD5:** `bb463a43fd61a3e7d2ebd2ebf30d13f0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.36 |
| Strings | 38 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 107.189.24.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | fef5f2ea17ceb16cc91b3e127f45a9de2ae3947c1529802216305f1022a86c8e | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
