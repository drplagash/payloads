# 🧬 Payload Analysis

`0017b2c894850ba3176c96f40103c5dfddfeae7d4a6bd5a71b869a74fcbbd9f5`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 2 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/0017b2c894850ba3176c96f40103c5dfddfeae7d4a6bd5a71b869a74fcbbd9f5.md](../../../../../malware-like/oraculo/botnet/0017b2c894850ba3176c96f40103c5dfddfeae7d4a6bd5a71b869a74fcbbd9f5.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0017b2c894850ba3176c96f40103c5dfddfeae7d4a6bd5a71b869a74fcbbd9f5`
- **SHA1:** `93c41c9811eef6a3c6594a8f3241876ca2a401ec`
- **MD5:** `02db9721eb10a650e4c058875c4de234`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.71 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://ogp[.]me/ns# | strings |
| hash | 0017b2c894850ba3176c96f40103c5dfddfeae7d4a6bd5a71b869a74fcbbd9f5 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
