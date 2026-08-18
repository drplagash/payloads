# 🧬 Payload Analysis

`11d3d191176682444516dd3275bf8474d3e8ab2a43b3d2acb888c7b1eae17c02`

## 📌 Resumen

Texto ASCII de 81 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/11d3d191176682444516dd3275bf8474d3e8ab2a43b3d2acb888c7b1eae17c02.md](../../../../../malware-like/oraculo/downloader/11d3d191176682444516dd3275bf8474d3e8ab2a43b3d2acb888c7b1eae17c02.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `11d3d191176682444516dd3275bf8474d3e8ab2a43b3d2acb888c7b1eae17c02`
- **MD5:** `f60d5877e7d447a7663dfb41f28e8ee2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 81 B |
| Entropía | 4.8 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 11d3d191176682444516dd3275bf8474d3e8ab2a43b3d2acb888c7b1eae17c02 | static_analysis |
| ip | 47.251.48.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
