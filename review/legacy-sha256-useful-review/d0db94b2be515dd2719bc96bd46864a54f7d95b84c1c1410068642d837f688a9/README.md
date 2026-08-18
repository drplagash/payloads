# 🧬 Payload Analysis

`d0db94b2be515dd2719bc96bd46864a54f7d95b84c1c1410068642d837f688a9`

## 📌 Resumen

Texto ASCII de 108 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d0db94b2be515dd2719bc96bd46864a54f7d95b84c1c1410068642d837f688a9.md](../../../../../malware-like/oraculo/downloader/d0db94b2be515dd2719bc96bd46864a54f7d95b84c1c1410068642d837f688a9.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d0db94b2be515dd2719bc96bd46864a54f7d95b84c1c1410068642d837f688a9`
- **MD5:** `e92c69d7ad27af8f081ab0da34fcf309`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 108 B |
| Entropía | 4.99 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.76.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| command | User-Agent: curl/7.76.1 | strings |
| hash | d0db94b2be515dd2719bc96bd46864a54f7d95b84c1c1410068642d837f688a9 | static_analysis |
| ip | 157.230.220.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
