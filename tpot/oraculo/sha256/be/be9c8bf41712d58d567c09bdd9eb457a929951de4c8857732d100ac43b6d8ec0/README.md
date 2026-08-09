# 🧬 Payload Analysis

`be9c8bf41712d58d567c09bdd9eb457a929951de4c8857732d100ac43b6d8ec0`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Se identificaron 5 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:32:58.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `be9c8bf41712d58d567c09bdd9eb457a929951de4c8857732d100ac43b6d8ec0`
- **SHA1:** `9345d03fe7ffccc67f2d7e32e9db39cdd51805c2`
- **MD5:** `a0d50992d7814070016c302a51bb272a`

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
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-armv7-static | strings |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-i686-static | strings |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-x86_64-static | strings |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-aarch64-static | strings |
| hash | be9c8bf41712d58d567c09bdd9eb457a929951de4c8857732d100ac43b6d8ec0 | static_analysis |
| ip | 34.147.30.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
