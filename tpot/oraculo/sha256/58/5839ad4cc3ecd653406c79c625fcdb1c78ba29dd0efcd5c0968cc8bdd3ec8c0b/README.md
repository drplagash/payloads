# 🧬 Payload Analysis

`5839ad4cc3ecd653406c79c625fcdb1c78ba29dd0efcd5c0968cc8bdd3ec8c0b`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/5839ad4cc3ecd653406c79c625fcdb1c78ba29dd0efcd5c0968cc8bdd3ec8c0b.md](../../../../../malware-like/oraculo/downloader/5839ad4cc3ecd653406c79c625fcdb1c78ba29dd0efcd5c0968cc8bdd3ec8c0b.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5839ad4cc3ecd653406c79c625fcdb1c78ba29dd0efcd5c0968cc8bdd3ec8c0b`
- **MD5:** `0fa804ef33e5d7a5d74654d5c948f6ec`

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
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 5839ad4cc3ecd653406c79c625fcdb1c78ba29dd0efcd5c0968cc8bdd3ec8c0b | static_analysis |
| ip | 47.250.150.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
