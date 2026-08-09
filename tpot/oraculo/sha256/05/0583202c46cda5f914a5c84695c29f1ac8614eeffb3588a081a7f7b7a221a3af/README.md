# 🧬 Payload Analysis

`0583202c46cda5f914a5c84695c29f1ac8614eeffb3588a081a7f7b7a221a3af`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 98 B. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0583202c46cda5f914a5c84695c29f1ac8614eeffb3588a081a7f7b7a221a3af`
- **MD5:** `df8df755b784760772c57bca8e3188a3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 98 B |
| Entropía | 5.1 |
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
| hash | 0583202c46cda5f914a5c84695c29f1ac8614eeffb3588a081a7f7b7a221a3af | static_analysis |
| ip | 51.75.255.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
