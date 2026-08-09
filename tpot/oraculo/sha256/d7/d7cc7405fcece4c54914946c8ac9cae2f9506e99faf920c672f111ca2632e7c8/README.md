# 🧬 Payload Analysis

`d7cc7405fcece4c54914946c8ac9cae2f9506e99faf920c672f111ca2632e7c8`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d7cc7405fcece4c54914946c8ac9cae2f9506e99faf920c672f111ca2632e7c8`
- **SHA1:** `243bdaf0fc9f21563295cab5fdc7b084b60e2b9e`
- **MD5:** `4cd59b92b68ac0c80b1fc1d4c8acc214`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.5 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.111.242.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | d7cc7405fcece4c54914946c8ac9cae2f9506e99faf920c672f111ca2632e7c8 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
