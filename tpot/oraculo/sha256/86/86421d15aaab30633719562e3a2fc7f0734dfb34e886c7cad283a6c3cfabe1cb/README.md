# 🧬 Payload Analysis

`86421d15aaab30633719562e3a2fc7f0734dfb34e886c7cad283a6c3cfabe1cb`

## 📌 Resumen

Texto ASCII de 82 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/86421d15aaab30633719562e3a2fc7f0734dfb34e886c7cad283a6c3cfabe1cb.md](../../../../../malware-like/oraculo/downloader/86421d15aaab30633719562e3a2fc7f0734dfb34e886c7cad283a6c3cfabe1cb.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `86421d15aaab30633719562e3a2fc7f0734dfb34e886c7cad283a6c3cfabe1cb`
- **MD5:** `ded3f082d483e4921c71d004179845ed`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 82 B |
| Entropía | 4.8 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 86421d15aaab30633719562e3a2fc7f0734dfb34e886c7cad283a6c3cfabe1cb | static_analysis |
| ip | 47.245.143.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
