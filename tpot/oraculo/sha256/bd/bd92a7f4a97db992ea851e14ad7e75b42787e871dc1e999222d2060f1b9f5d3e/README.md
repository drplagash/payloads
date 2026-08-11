# 🧬 Payload Analysis

`bd92a7f4a97db992ea851e14ad7e75b42787e871dc1e999222d2060f1b9f5d3e`

## 📌 Resumen

Texto ASCII de 91 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/bd92a7f4a97db992ea851e14ad7e75b42787e871dc1e999222d2060f1b9f5d3e.md](../../../../../malware-like/oraculo/downloader/bd92a7f4a97db992ea851e14ad7e75b42787e871dc1e999222d2060f1b9f5d3e.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bd92a7f4a97db992ea851e14ad7e75b42787e871dc1e999222d2060f1b9f5d3e`
- **MD5:** `e8f055c9ad9fd974179145ca07e40d70`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 91 B |
| Entropía | 5 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.68.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.68.0 | strings |
| hash | bd92a7f4a97db992ea851e14ad7e75b42787e871dc1e999222d2060f1b9f5d3e | static_analysis |
| ip | 185.242.226.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
