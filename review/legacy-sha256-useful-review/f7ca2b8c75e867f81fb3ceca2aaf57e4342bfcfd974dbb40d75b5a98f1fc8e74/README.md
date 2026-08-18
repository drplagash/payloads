# 🧬 Payload Analysis

`f7ca2b8c75e867f81fb3ceca2aaf57e4342bfcfd974dbb40d75b5a98f1fc8e74`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f7ca2b8c75e867f81fb3ceca2aaf57e4342bfcfd974dbb40d75b5a98f1fc8e74.md](../../../../../malware-like/oraculo/downloader/f7ca2b8c75e867f81fb3ceca2aaf57e4342bfcfd974dbb40d75b5a98f1fc8e74.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f7ca2b8c75e867f81fb3ceca2aaf57e4342bfcfd974dbb40d75b5a98f1fc8e74`
- **MD5:** `bc4a2c14560ed958cd30c3f3361118c2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.75 |
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
| hash | f7ca2b8c75e867f81fb3ceca2aaf57e4342bfcfd974dbb40d75b5a98f1fc8e74 | static_analysis |
| ip | 47.251.244.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
