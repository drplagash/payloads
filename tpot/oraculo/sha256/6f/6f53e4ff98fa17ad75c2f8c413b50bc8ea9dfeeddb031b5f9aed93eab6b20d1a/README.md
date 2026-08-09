# 🧬 Payload Analysis

`6f53e4ff98fa17ad75c2f8c413b50bc8ea9dfeeddb031b5f9aed93eab6b20d1a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:32:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6f53e4ff98fa17ad75c2f8c413b50bc8ea9dfeeddb031b5f9aed93eab6b20d1a`
- **SHA1:** `712e578b5adeb44bcc7adeee22a7989515fde631`
- **MD5:** `c6ebfd00747c30372316581607c4f69f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 224 B |
| Entropía | 5.26 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 6f53e4ff98fa17ad75c2f8c413b50bc8ea9dfeeddb031b5f9aed93eab6b20d1a | static_analysis |
| ip | 193.176.31.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
