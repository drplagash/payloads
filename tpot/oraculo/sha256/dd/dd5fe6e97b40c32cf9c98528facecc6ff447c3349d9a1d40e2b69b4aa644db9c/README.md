# 🧬 Payload Analysis

`dd5fe6e97b40c32cf9c98528facecc6ff447c3349d9a1d40e2b69b4aa644db9c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dd5fe6e97b40c32cf9c98528facecc6ff447c3349d9a1d40e2b69b4aa644db9c`
- **SHA1:** `cb302e79b2d4011fb859a899cec2aade8550a8e8`
- **MD5:** `84d5446089b0c8c9db86ae35b38767fb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 444 B |
| Entropía | 5.56 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| hash | dd5fe6e97b40c32cf9c98528facecc6ff447c3349d9a1d40e2b69b4aa644db9c | static_analysis |
| ip | 5.61.209.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
