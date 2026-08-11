# 🧬 Payload Analysis

`7b50b6abc186824ed1b985ef9a62c340bef1f8afa356188ffb7a58989882f020`

## 📌 Resumen

Texto ASCII de 620 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m` en `hxxp://[internal-ip-redacted]:8088/Mozi.m`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/7b50b6abc186824ed1b985ef9a62c340bef1f8afa356188ffb7a58989882f020.md](../../../../../malware-like/oraculo/downloader/7b50b6abc186824ed1b985ef9a62c340bef1f8afa356188ffb7a58989882f020.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7b50b6abc186824ed1b985ef9a62c340bef1f8afa356188ffb7a58989882f020`
- **SHA1:** `541fe28d277d390cb3d5a5bf49aa33f332cb6f1b`
- **MD5:** `97008d592ad7aa00dc123caaf8b3243c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (620), with no line terminators |
| Tamaño | 620 B |
| Entropía | 5.37 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (620), with no line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]:8088/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | 7b50b6abc186824ed1b985ef9a62c340bef1f8afa356188ffb7a58989882f020 | static_analysis |
| ip | 202.141.94.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
