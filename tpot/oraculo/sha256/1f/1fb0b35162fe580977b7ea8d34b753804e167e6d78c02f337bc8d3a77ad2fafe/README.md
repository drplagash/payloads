# 🧬 Payload Analysis

`1fb0b35162fe580977b7ea8d34b753804e167e6d78c02f337bc8d3a77ad2fafe`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/1fb0b35162fe580977b7ea8d34b753804e167e6d78c02f337bc8d3a77ad2fafe.md](../../../../../malware-like/oraculo/downloader/1fb0b35162fe580977b7ea8d34b753804e167e6d78c02f337bc8d3a77ad2fafe.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:40:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1fb0b35162fe580977b7ea8d34b753804e167e6d78c02f337bc8d3a77ad2fafe`
- **MD5:** `4b4a38ab608c255d32570d61d0d9ebce`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.76 |
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
| hash | 1fb0b35162fe580977b7ea8d34b753804e167e6d78c02f337bc8d3a77ad2fafe | static_analysis |
| ip | 47.251.178.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
