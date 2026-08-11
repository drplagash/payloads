# 🧬 Payload Analysis

`f5cc564e6b4c8de121c84d177083c5545de692ecae85f45871e6726bd95c0011`

## 📌 Resumen

Texto ASCII de 84 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. **C2 / infraestructura de control:**

- **Posible C2:** `112.118.103.XXX` — confianza Descartado, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f5cc564e6b4c8de121c84d177083c5545de692ecae85f45871e6726bd95c0011.md](../../../../../malware-like/oraculo/downloader/f5cc564e6b4c8de121c84d177083c5545de692ecae85f45871e6726bd95c0011.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:03:20.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f5cc564e6b4c8de121c84d177083c5545de692ecae85f45871e6726bd95c0011`
- **SHA1:** `f5a9d5eeb8aaccdd76171fa5c0a39e9ebc7df14e`
- **MD5:** `0784fa411a534b484fbab6f48c65715d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
| Entropía | 4.82 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.81.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 112.118.103.XXX | static_analysis |
| command | User-Agent: curl/7.81.0 | strings |
| hash | f5cc564e6b4c8de121c84d177083c5545de692ecae85f45871e6726bd95c0011 | static_analysis |
| ip | 47.251.123.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
