# 🧬 Payload Analysis

`cee53c0f2f8addbe4cc1352034c2bd74528b9520ebde97ee8f53a5f146e61172`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 120 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `index2.asp` en `hxxp://190.179.144.XXX:80/cgi-bin/index2.asp`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:48:49.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cee53c0f2f8addbe4cc1352034c2bd74528b9520ebde97ee8f53a5f146e61172`
- **SHA1:** `ecb263119647a667536c6e63c5ea4199da9e32cd`
- **MD5:** `bef01d3f6cef4cdc14a205ed27d4031b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 120 B |
| Entropía | 5.03 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://190.179.144.XXX:80/cgi-bin/index2.asp | strings |
| ip | 190.179.144.XXX | static_analysis |
| hash | cee53c0f2f8addbe4cc1352034c2bd74528b9520ebde97ee8f53a5f146e61172 | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
