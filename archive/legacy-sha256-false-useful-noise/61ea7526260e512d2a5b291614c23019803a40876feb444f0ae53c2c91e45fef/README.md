# 🧬 Payload Analysis

`61ea7526260e512d2a5b291614c23019803a40876feb444f0ae53c2c91e45fef`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/downloader/61ea7526260e512d2a5b291614c23019803a40876feb444f0ae53c2c91e45fef.md](../../../../../malware-like/oraculo/downloader/61ea7526260e512d2a5b291614c23019803a40876feb444f0ae53c2c91e45fef.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:39:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `61ea7526260e512d2a5b291614c23019803a40876feb444f0ae53c2c91e45fef`
- **MD5:** `43e9f88b1b9a0f4e3b9793c266b3db32`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.71 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/1999/xlink | strings |
| url | hxxp://www[.]w3[.]org/2000/svg | strings |
| hash | 61ea7526260e512d2a5b291614c23019803a40876feb444f0ae53c2c91e45fef | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
