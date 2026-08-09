# 🧬 Payload Analysis

`d0930c51fee071f01a93e7f7991783f52dd72a468f2de0fde7e8a8223e397cea`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 140 B. La evidencia estática disponible identifica capacidad de descarga remota. Se extrajo como destino remoto `hxxp://azenv[.]net/`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:03.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d0930c51fee071f01a93e7f7991783f52dd72a468f2de0fde7e8a8223e397cea`
- **MD5:** `63bfbd452aeda5b81cfea7c9f15053e4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 140 B |
| Entropía | 4.85 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://azenv[.]net/ | strings |
| hash | d0930c51fee071f01a93e7f7991783f52dd72a468f2de0fde7e8a8223e397cea | static_analysis |
| ip | 91.92.42.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
