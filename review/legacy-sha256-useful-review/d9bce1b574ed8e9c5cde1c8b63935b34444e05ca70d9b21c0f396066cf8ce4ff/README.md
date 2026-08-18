# 🧬 Payload Analysis

`d9bce1b574ed8e9c5cde1c8b63935b34444e05ca70d9b21c0f396066cf8ce4ff`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d9bce1b574ed8e9c5cde1c8b63935b34444e05ca70d9b21c0f396066cf8ce4ff.md](../../../../../malware-like/oraculo/downloader/d9bce1b574ed8e9c5cde1c8b63935b34444e05ca70d9b21c0f396066cf8ce4ff.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d9bce1b574ed8e9c5cde1c8b63935b34444e05ca70d9b21c0f396066cf8ce4ff`
- **MD5:** `c188dfeec3c1fcfec386a2b449c4c3aa`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.82 |
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
| hash | d9bce1b574ed8e9c5cde1c8b63935b34444e05ca70d9b21c0f396066cf8ce4ff | static_analysis |
| ip | 47.89.193.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
