# 🧬 Payload Analysis

`9c49561f4ba69dea4afd03df0f57c0ba69849f343dceca49245912af4b9700fc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:16+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9c49561f4ba69dea4afd03df0f57c0ba69849f343dceca49245912af4b9700fc`
- **SHA1:** `493bbd77f4ecdb0b0af3447bc3ccd61f5cd26fb0`
- **MD5:** `640441928da3c0d3e52ba578ccc75889`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.48 |
| Strings | 33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 107.189.26.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | 9c49561f4ba69dea4afd03df0f57c0ba69849f343dceca49245912af4b9700fc | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
