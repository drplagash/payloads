# 🧬 Payload Analysis

`1d111c535a9a3f21f0efa338fdff215b87e2bd2e8750d9461c6999e74b1b3628`

## 📌 Resumen

Texto ASCII de 834 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 2 comandos observados o extraídos. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/1d111c535a9a3f21f0efa338fdff215b87e2bd2e8750d9461c6999e74b1b3628.md](../../../../../malware-like/oraculo/downloader/1d111c535a9a3f21f0efa338fdff215b87e2bd2e8750d9461c6999e74b1b3628.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1d111c535a9a3f21f0efa338fdff215b87e2bd2e8750d9461c6999e74b1b3628`
- **MD5:** `02cf48f8d587bb0d856a6c063bbafb47`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 834 B |
| Entropía | 5.11 |
| Strings | 36 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
GET /wget.sh HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 94.154.43.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| command | GET /wget.sh HTTP/1.1 | strings |
| hash | 1d111c535a9a3f21f0efa338fdff215b87e2bd2e8750d9461c6999e74b1b3628 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
