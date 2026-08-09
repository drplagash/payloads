# 🧬 Payload Analysis

`178df892755b026273c2e37ab4dd26427ebe05b47be164544db4c053f5bbb2c5`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `178df892755b026273c2e37ab4dd26427ebe05b47be164544db4c053f5bbb2c5`
- **SHA1:** `81fb12ee3ef9ed758545bfc56f835c76479f2f97`
- **MD5:** `75ec3005121190b008555f1e6366f6d1`

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
| ip | 153.75.90.XXX | static_analysis |
| ip | 190.179.153.XXX | static_analysis |
| hash | 178df892755b026273c2e37ab4dd26427ebe05b47be164544db4c053f5bbb2c5 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
