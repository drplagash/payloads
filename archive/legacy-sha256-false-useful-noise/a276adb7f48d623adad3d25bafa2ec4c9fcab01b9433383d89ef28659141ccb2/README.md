# 🧬 Payload Analysis

`a276adb7f48d623adad3d25bafa2ec4c9fcab01b9433383d89ef28659141ccb2`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/a276adb7f48d623adad3d25bafa2ec4c9fcab01b9433383d89ef28659141ccb2.md](../../../../../malware-like/oraculo/botnet/a276adb7f48d623adad3d25bafa2ec4c9fcab01b9433383d89ef28659141ccb2.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:35:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a276adb7f48d623adad3d25bafa2ec4c9fcab01b9433383d89ef28659141ccb2`
- **MD5:** `9db222b73be3c5287dc851135fe621c3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.51 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | a276adb7f48d623adad3d25bafa2ec4c9fcab01b9433383d89ef28659141ccb2 | static_analysis |
| ip | 183.105.3.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
