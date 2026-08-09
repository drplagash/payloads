# 🧬 Payload Analysis

`ec2b1e1a9769b55e90a42d4f6a2da471bdcbf2092cd507b8717bd6a25bb001e1`

## 📌 Resumen

Artefacto de 787 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.51. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ec2b1e1a9769b55e90a42d4f6a2da471bdcbf2092cd507b8717bd6a25bb001e1`
- **SHA1:** `43f50259a7e4dbdc1194f8cf14388e749d7b2024`
- **MD5:** `391b1d76c4010ca87b20cf6baa49baf0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 787 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 32.95.32.XXX | static_analysis |
| hash | ec2b1e1a9769b55e90a42d4f6a2da471bdcbf2092cd507b8717bd6a25bb001e1 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
