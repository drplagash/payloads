# 🧬 Payload Analysis

`76be38af51bed44e83a85ecd5432eb53f04d1d597497ff2eb98a083fd5a26467`

## 📌 Resumen

Texto ASCII de 587 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/76be38af51bed44e83a85ecd5432eb53f04d1d597497ff2eb98a083fd5a26467.md](../../../../../malware-like/oraculo/downloader/76be38af51bed44e83a85ecd5432eb53f04d1d597497ff2eb98a083fd5a26467.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `76be38af51bed44e83a85ecd5432eb53f04d1d597497ff2eb98a083fd5a26467`
- **SHA1:** `2936f0f4908e2088d4b7bf2c9881ed25474f7413`
- **MD5:** `3df08e1712a735a468e558290da70ef7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (471), with CRLF line terminators |
| Tamaño | 587 B |
| Entropía | 5.53 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (471), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | 76be38af51bed44e83a85ecd5432eb53f04d1d597497ff2eb98a083fd5a26467 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
