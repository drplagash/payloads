# 🧬 Payload Analysis

`b127767f9dda4a7c88a5e4d2ea75d8b199e7c4d9aef4ace35915a5fabafae5d4`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 414 B. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 2 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b127767f9dda4a7c88a5e4d2ea75d8b199e7c4d9aef4ace35915a5fabafae5d4`
- **MD5:** `134f1131c34828623f7c2103d7bd5fb1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 414 B |
| Entropía | 5.11 |
| Strings | 18 |

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
| hash | b127767f9dda4a7c88a5e4d2ea75d8b199e7c4d9aef4ace35915a5fabafae5d4 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
