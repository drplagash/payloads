# 🧬 Payload Analysis

`14f079f4af0c564319c53cf0cbf88edba2b9ea74c1e18b9304756756126dde03`

## 📌 Resumen

Texto ASCII de 1.2 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `x86` en `hxxp://217.60.195.XXX:8080/x86`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/14f079f4af0c564319c53cf0cbf88edba2b9ea74c1e18b9304756756126dde03.md](../../../../../malware-like/oraculo/downloader/14f079f4af0c564319c53cf0cbf88edba2b9ea74c1e18b9304756756126dde03.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:41:09.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `14f079f4af0c564319c53cf0cbf88edba2b9ea74c1e18b9304756756126dde03`
- **SHA1:** `dc9eab6d9274c0daaa01ceecc39e9732a5036393`
- **MD5:** `b575a2d459e2058343498eac3d5f536f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (480), with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.76 |
| Strings | 18 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (480), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://217.60.195.XXX:8080/x86; | strings |
| ip | 190.179.166.XXX | static_analysis |
| ip | 217.60.195.XXX | static_analysis |
| hash | 14f079f4af0c564319c53cf0cbf88edba2b9ea74c1e18b9304756756126dde03 | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
