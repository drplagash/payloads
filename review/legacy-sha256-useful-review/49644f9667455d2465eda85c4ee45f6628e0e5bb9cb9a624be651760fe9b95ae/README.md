# 🧬 Payload Analysis

`49644f9667455d2465eda85c4ee45f6628e0e5bb9cb9a624be651760fe9b95ae`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/49644f9667455d2465eda85c4ee45f6628e0e5bb9cb9a624be651760fe9b95ae.md](../../../../../malware-like/oraculo/downloader/49644f9667455d2465eda85c4ee45f6628e0e5bb9cb9a624be651760fe9b95ae.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `49644f9667455d2465eda85c4ee45f6628e0e5bb9cb9a624be651760fe9b95ae`
- **MD5:** `18a38e8c1780ebdac2345a4ac88e7bc8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.77 |
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
| ip | 190.179.167.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 49644f9667455d2465eda85c4ee45f6628e0e5bb9cb9a624be651760fe9b95ae | static_analysis |
| ip | 47.84.135.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
