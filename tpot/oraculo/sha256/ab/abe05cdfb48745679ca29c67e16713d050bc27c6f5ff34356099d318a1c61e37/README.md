# 🧬 Payload Analysis

`abe05cdfb48745679ca29c67e16713d050bc27c6f5ff34356099d318a1c61e37`

## 📌 Resumen

Artefacto de 1.4 KiB. La evidencia estática disponible identifica capacidad de descarga remota. Se extrajo como destino remoto `hxxps://raw[.]githubusercontent[.]co`. Se extrajeron 2 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:20.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `abe05cdfb48745679ca29c67e16713d050bc27c6f5ff34356099d318a1c61e37`
- **SHA1:** `ba08883f6611929beaba52f6f418be10498f7235`
- **MD5:** `b456582669d686f3203efbda6f65073b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 5.51 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://raw[.]githubusercontent[.]co | strings |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-aarch64-static | strings |
| hash | abe05cdfb48745679ca29c67e16713d050bc27c6f5ff34356099d318a1c61e37 | static_analysis |
| ip | 34.106.128.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
