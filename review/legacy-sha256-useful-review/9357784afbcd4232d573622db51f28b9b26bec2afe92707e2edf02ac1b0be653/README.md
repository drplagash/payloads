# 🧬 Payload Analysis

`9357784afbcd4232d573622db51f28b9b26bec2afe92707e2edf02ac1b0be653`

## 📌 Resumen

Texto ASCII de 103 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/9357784afbcd4232d573622db51f28b9b26bec2afe92707e2edf02ac1b0be653.md](../../../../../malware-like/oraculo/downloader/9357784afbcd4232d573622db51f28b9b26bec2afe92707e2edf02ac1b0be653.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9357784afbcd4232d573622db51f28b9b26bec2afe92707e2edf02ac1b0be653`
- **MD5:** `0b2c374ea2b0316009343b3ee9a2375d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 103 B |
| Entropía | 4.99 |
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
| hash | 9357784afbcd4232d573622db51f28b9b26bec2afe92707e2edf02ac1b0be653 | static_analysis |
| ip | 51.75.255.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
