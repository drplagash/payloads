# 🧬 Payload Analysis

`276c9904d8477a2a260aeeea50f6fd6bf502ddeb2fa0bfb16e3b7e536ea098b5`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 274 B. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `276c9904d8477a2a260aeeea50f6fd6bf502ddeb2fa0bfb16e3b7e536ea098b5`
- **MD5:** `39a5596d21320d305e10e5cbc0c54b0b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 274 B |
| Entropía | 5.11 |
| Strings | 12 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 94.154.43.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 276c9904d8477a2a260aeeea50f6fd6bf502ddeb2fa0bfb16e3b7e536ea098b5 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
