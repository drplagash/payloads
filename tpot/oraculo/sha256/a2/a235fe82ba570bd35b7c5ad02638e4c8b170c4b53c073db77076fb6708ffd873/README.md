# 🧬 Payload Analysis

`a235fe82ba570bd35b7c5ad02638e4c8b170c4b53c073db77076fb6708ffd873`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a235fe82ba570bd35b7c5ad02638e4c8b170c4b53c073db77076fb6708ffd873`
- **SHA1:** `e9041f8993be5558aadbb3e78ee69884421b6d59`
- **MD5:** `cfa008be680b11b53cc4a13c5908fcd5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 171 B |
| Entropía | 5.12 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /tmp/.env HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| ip | 190.179.169.XXX | static_analysis |
| command | GET /tmp/.env HTTP/1.1 | strings |
| hash | a235fe82ba570bd35b7c5ad02638e4c8b170c4b53c073db77076fb6708ffd873 | static_analysis |
| ip | 151.243.18.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
