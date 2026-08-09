# 🧬 Payload Analysis

`237847fad5459c8cc8f3e7dd285851caeeeb8e7e9577628cb08c195e512433bd`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `237847fad5459c8cc8f3e7dd285851caeeeb8e7e9577628cb08c195e512433bd`
- **MD5:** `94535a0f62bfc4f164e84bf510a030ce`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 200 B |
| Entropía | 5.09 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.38.0
User-Agent: Wget/1.25.0 (linux-gnu)
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 31.56.209.XXX | static_analysis |
| hash | 237847fad5459c8cc8f3e7dd285851caeeeb8e7e9577628cb08c195e512433bd | static_analysis |
| command | User-Agent: curl/7.38.0 | strings |
| command | User-Agent: Wget/1.25.0 (linux-gnu) | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
