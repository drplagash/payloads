# 🧬 Payload Analysis

`e8154e8edf7c6b057c5c68505e8049fbe6a5c53bdbc811f2bbc0bc24e1fe01eb`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 555 B. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 2 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e8154e8edf7c6b057c5c68505e8049fbe6a5c53bdbc811f2bbc0bc24e1fe01eb`
- **MD5:** `640bd7d22a45c53bd1e78adfaeb1d545`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 555 B |
| Entropía | 5.12 |
| Strings | 24 |

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
| hash | e8154e8edf7c6b057c5c68505e8049fbe6a5c53bdbc811f2bbc0bc24e1fe01eb | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
