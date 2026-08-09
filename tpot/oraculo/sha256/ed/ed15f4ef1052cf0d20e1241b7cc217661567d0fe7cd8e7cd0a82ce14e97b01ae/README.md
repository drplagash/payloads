# 🧬 Payload Analysis

`ed15f4ef1052cf0d20e1241b7cc217661567d0fe7cd8e7cd0a82ce14e97b01ae`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ed15f4ef1052cf0d20e1241b7cc217661567d0fe7cd8e7cd0a82ce14e97b01ae`
- **SHA1:** `b5790b1c922699523274255ba377006a39a43f93`
- **MD5:** `21b7d012ae45d05e7b44751eaf3cd252`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 548 B |
| Entropía | 5.39 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | ed15f4ef1052cf0d20e1241b7cc217661567d0fe7cd8e7cd0a82ce14e97b01ae | static_analysis |
| ip | 141.98.11.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
