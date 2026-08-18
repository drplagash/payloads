# 🧬 Payload Analysis

`2d9fb4857f5a184bee5a16ca9a71b213635c95681dd6fec21bb052b588e293d2`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 5 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/2d9fb4857f5a184bee5a16ca9a71b213635c95681dd6fec21bb052b588e293d2.md](../../../../../malware-like/oraculo/botnet/2d9fb4857f5a184bee5a16ca9a71b213635c95681dd6fec21bb052b588e293d2.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:08:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2d9fb4857f5a184bee5a16ca9a71b213635c95681dd6fec21bb052b588e293d2`
- **SHA1:** `d1a43ca781ea9cea19598e10a290b7ab464013c2`
- **MD5:** `a92fd3cad308f879cac353d66a9d58ae`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 653 B |
| Entropía | 5.27 |
| Strings | 20 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://www[.]google[.]com/ | strings |
| url | hxxps://alfabienes[.]com[.]co/gambling | strings |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| ip | 66.249.91.XXX | static_analysis |
| hash | 2d9fb4857f5a184bee5a16ca9a71b213635c95681dd6fec21bb052b588e293d2 | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
