# 🧬 Payload Analysis

`85ff23986a7ec5f7789404a9b37433a9b77a3ae60fb832b3743d31539e29f610`

## 📌 Resumen

Texto ASCII de 694 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 2 comandos observados o extraídos. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/85ff23986a7ec5f7789404a9b37433a9b77a3ae60fb832b3743d31539e29f610.md](../../../../../malware-like/oraculo/downloader/85ff23986a7ec5f7789404a9b37433a9b77a3ae60fb832b3743d31539e29f610.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `85ff23986a7ec5f7789404a9b37433a9b77a3ae60fb832b3743d31539e29f610`
- **MD5:** `f5e94a73d4c0978a54ad3c7f0cc05a54`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 694 B |
| Entropía | 5.12 |
| Strings | 30 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)

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
| hash | 85ff23986a7ec5f7789404a9b37433a9b77a3ae60fb832b3743d31539e29f610 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
