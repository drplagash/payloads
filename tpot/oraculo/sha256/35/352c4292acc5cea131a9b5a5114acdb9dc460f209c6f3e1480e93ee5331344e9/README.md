# 🧬 Payload Analysis

`352c4292acc5cea131a9b5a5114acdb9dc460f209c6f3e1480e93ee5331344e9`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:20+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `352c4292acc5cea131a9b5a5114acdb9dc460f209c6f3e1480e93ee5331344e9`
- **SHA1:** `05dee7ea1af10c7f1c820553dd7a7dbf883680e7`
- **MD5:** `838c0cce9c11e717388adc10bd18f66d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 24 B |
| Entropía | 4.3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 352c4292acc5cea131a9b5a5114acdb9dc460f209c6f3e1480e93ee5331344e9 | static_analysis |
| ip | 193.46.255.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
