# 🧬 Payload Analysis

`d9bf3e84ff5b58fcef07efb423a27d6bde2308bd4165c0f42f332e64d3d29e01`

## 📌 Resumen

Texto ASCII de 415 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 2 comandos observados o extraídos. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d9bf3e84ff5b58fcef07efb423a27d6bde2308bd4165c0f42f332e64d3d29e01.md](../../../../../malware-like/oraculo/downloader/d9bf3e84ff5b58fcef07efb423a27d6bde2308bd4165c0f42f332e64d3d29e01.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d9bf3e84ff5b58fcef07efb423a27d6bde2308bd4165c0f42f332e64d3d29e01`
- **MD5:** `33cd505119aa1ca0df6a87820aac5033`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 415 B |
| Entropía | 5.12 |
| Strings | 18 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
GET /wget.sh HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 31.56.209.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| command | GET /wget.sh HTTP/1.1 | strings |
| hash | d9bf3e84ff5b58fcef07efb423a27d6bde2308bd4165c0f42f332e64d3d29e01 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
