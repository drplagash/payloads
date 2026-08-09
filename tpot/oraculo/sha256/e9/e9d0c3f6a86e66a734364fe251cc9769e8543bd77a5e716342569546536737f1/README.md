# 🧬 Payload Analysis

`e9d0c3f6a86e66a734364fe251cc9769e8543bd77a5e716342569546536737f1`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Se identificaron 5 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:36:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e9d0c3f6a86e66a734364fe251cc9769e8543bd77a5e716342569546536737f1`
- **SHA1:** `2ab041979797ad42409500f7e2c800de0ef1d0f9`
- **MD5:** `cf9c855f99856ae89615d932c65c34fa`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 5.55 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://gitlab[.]com/Kanedias/xmrig-static/-/releases/permalink/latest/downloads/xmrig-armv7-static | strings |
| url | hxxps://gitlab[.]com/Kanedias/xmrig-static/-/releases/permalink/latest/downloads/xmrig-x86_64-static | strings |
| url | hxxps://gitlab[.]com/Kanedias/xmrig-static/-/releases/permalink/latest/downloads/xmrig-aarch64-static | strings |
| url | hxxps://gitlab[.]com/Kanedias/xmrig-static/-/releases/permalink/latest/downloads/xmrig-i686-static | strings |
| hash | e9d0c3f6a86e66a734364fe251cc9769e8543bd77a5e716342569546536737f1 | static_analysis |
| ip | 136.109.178.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
