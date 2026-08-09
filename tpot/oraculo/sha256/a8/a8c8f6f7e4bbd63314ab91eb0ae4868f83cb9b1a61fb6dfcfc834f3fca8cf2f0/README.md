# 🧬 Payload Analysis

`a8c8f6f7e4bbd63314ab91eb0ae4868f83cb9b1a61fb6dfcfc834f3fca8cf2f0`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:12+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a8c8f6f7e4bbd63314ab91eb0ae4868f83cb9b1a61fb6dfcfc834f3fca8cf2f0`
- **MD5:** `6e4fcfc4f9d77668dbbc7cf93b67bcc6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 129 B |
| Entropía | 5.11 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.175.XXX | static_analysis |
| hash | a8c8f6f7e4bbd63314ab91eb0ae4868f83cb9b1a61fb6dfcfc834f3fca8cf2f0 | static_analysis |
| ip | 221.130.29.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
