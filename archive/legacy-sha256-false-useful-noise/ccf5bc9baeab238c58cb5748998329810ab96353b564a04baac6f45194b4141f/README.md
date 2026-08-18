# 🧬 Payload Analysis

`ccf5bc9baeab238c58cb5748998329810ab96353b564a04baac6f45194b4141f`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/ccf5bc9baeab238c58cb5748998329810ab96353b564a04baac6f45194b4141f.md](../../../../../malware-like/oraculo/botnet/ccf5bc9baeab238c58cb5748998329810ab96353b564a04baac6f45194b4141f.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:49:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ccf5bc9baeab238c58cb5748998329810ab96353b564a04baac6f45194b4141f`
- **SHA1:** `7d108946770a4462d999b23b16aea34317047430`
- **MD5:** `6e965441ffd566adddca67eb0a9a9d66`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 169 B |
| Entropía | 5.14 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://about[.]censys[.]io/) | strings |
| ip | 190.179.144.XXX | static_analysis |
| hash | ccf5bc9baeab238c58cb5748998329810ab96353b564a04baac6f45194b4141f | static_analysis |
| ip | 66.132.195.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
