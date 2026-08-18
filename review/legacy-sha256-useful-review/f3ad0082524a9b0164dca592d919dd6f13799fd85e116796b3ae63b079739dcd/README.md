# 🧬 Payload Analysis

`f3ad0082524a9b0164dca592d919dd6f13799fd85e116796b3ae63b079739dcd`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f3ad0082524a9b0164dca592d919dd6f13799fd85e116796b3ae63b079739dcd.md](../../../../../malware-like/oraculo/downloader/f3ad0082524a9b0164dca592d919dd6f13799fd85e116796b3ae63b079739dcd.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f3ad0082524a9b0164dca592d919dd6f13799fd85e116796b3ae63b079739dcd`
- **MD5:** `df7de7051adc256ba4d5e53200613db0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.78 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | f3ad0082524a9b0164dca592d919dd6f13799fd85e116796b3ae63b079739dcd | static_analysis |
| ip | 47.251.250.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
