# 🧬 Payload Analysis

`3701986ef43992b6b37bdb1b5e97d89b7a4ce9572a0fa8b4c7860cc4399fbdbb`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 133 B. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3701986ef43992b6b37bdb1b5e97d89b7a4ce9572a0fa8b4c7860cc4399fbdbb`
- **MD5:** `e170406080b1eaccada9ebf1a3858821`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 133 B |
| Entropía | 5.16 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/8.5.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| command | User-Agent: curl/8.5.0 | strings |
| hash | 3701986ef43992b6b37bdb1b5e97d89b7a4ce9572a0fa8b4c7860cc4399fbdbb | static_analysis |
| ip | 51.75.255.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
