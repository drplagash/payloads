# 🧬 Payload Analysis

`62ce54f55e327dd64c7959fdb900c993b8ee7a08b8719dbc46967202e51f24ed`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:06:31+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `62ce54f55e327dd64c7959fdb900c993b8ee7a08b8719dbc46967202e51f24ed`
- **SHA1:** `ad065d025ea58b78bd7dafea7f9feab9d860b0c5`
- **MD5:** `f7117ad887d356930efc5edf791142f8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 397 B |
| Entropía | 5.43 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 199.178.143.XXX | static_analysis |
| url | hxxps://qmhsex[.]com/ | strings |
| url | hxxps://www[.]kkkkk[.]ph/?s=microgaming&ref=345907&aff=229&click=10601738&utm_source=vnsextop1.com&utm_medium=affiliate&utm_campaign=microgaming | strings |
| hash | 62ce54f55e327dd64c7959fdb900c993b8ee7a08b8719dbc46967202e51f24ed | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
