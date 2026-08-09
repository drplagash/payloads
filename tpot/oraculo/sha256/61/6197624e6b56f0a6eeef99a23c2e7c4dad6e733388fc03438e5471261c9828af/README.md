# 🧬 Payload Analysis

`6197624e6b56f0a6eeef99a23c2e7c4dad6e733388fc03438e5471261c9828af`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Se identificaron 5 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6197624e6b56f0a6eeef99a23c2e7c4dad6e733388fc03438e5471261c9828af`
- **SHA1:** `089b654edd0fb4c67b3d3bbae482b45b8858693b`
- **MD5:** `e9ace9277baf0219572a4a471c107023`

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
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-aarch64-static | strings |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-x86_64-static | strings |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-armv7-static | strings |
| hash | 6197624e6b56f0a6eeef99a23c2e7c4dad6e733388fc03438e5471261c9828af | static_analysis |
| ip | 34.16.220.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
