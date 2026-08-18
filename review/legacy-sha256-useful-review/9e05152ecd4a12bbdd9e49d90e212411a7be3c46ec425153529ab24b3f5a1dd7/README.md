# 🧬 Payload Analysis

`9e05152ecd4a12bbdd9e49d90e212411a7be3c46ec425153529ab24b3f5a1dd7`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/9e05152ecd4a12bbdd9e49d90e212411a7be3c46ec425153529ab24b3f5a1dd7.md](../../../../../malware-like/oraculo/downloader/9e05152ecd4a12bbdd9e49d90e212411a7be3c46ec425153529ab24b3f5a1dd7.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9e05152ecd4a12bbdd9e49d90e212411a7be3c46ec425153529ab24b3f5a1dd7`
- **MD5:** `8417b416ba4f5e44003f69d4da10f0b4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.75 |
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
| hash | 9e05152ecd4a12bbdd9e49d90e212411a7be3c46ec425153529ab24b3f5a1dd7 | static_analysis |
| ip | 47.74.13.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
