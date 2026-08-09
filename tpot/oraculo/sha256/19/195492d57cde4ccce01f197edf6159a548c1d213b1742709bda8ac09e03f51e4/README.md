# 🧬 Payload Analysis

`195492d57cde4ccce01f197edf6159a548c1d213b1742709bda8ac09e03f51e4`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 99 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `robertdavidgraham` en `hxxps://github[.]com/robertdavidgraham/`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `195492d57cde4ccce01f197edf6159a548c1d213b1742709bda8ac09e03f51e4`
- **SHA1:** `328770cd1ae7402407668d16b01b5af077da0c8a`
- **MD5:** `9fa5c8277e259bdcc9d01a9dbc58b4f6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 99 B |
| Entropía | 4.9 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://github[.]com/robertdavidgraham/ | strings |
| hash | 195492d57cde4ccce01f197edf6159a548c1d213b1742709bda8ac09e03f51e4 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
