# 🧬 Payload Analysis

`936a6d271529567b808147e615fd12e07e3c6057e2710047daa3491284a5ed93`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Se identificaron 5 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:59.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `936a6d271529567b808147e615fd12e07e3c6057e2710047daa3491284a5ed93`
- **SHA1:** `acc6dd897a383cc9d5ff9ae65119fed6ec6c3278`
- **MD5:** `4793cfcddd22cace47beee8f5f80fc58`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 5.62 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-i686-static | strings |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-armv7-static | strings |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-aarch64-static | strings |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-x86_64-static | strings |
| hash | 936a6d271529567b808147e615fd12e07e3c6057e2710047daa3491284a5ed93 | static_analysis |
| ip | 35.185.69.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
