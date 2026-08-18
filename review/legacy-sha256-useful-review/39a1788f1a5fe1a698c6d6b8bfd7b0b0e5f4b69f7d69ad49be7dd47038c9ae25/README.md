# 🧬 Payload Analysis

`39a1788f1a5fe1a698c6d6b8bfd7b0b0e5f4b69f7d69ad49be7dd47038c9ae25`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/39a1788f1a5fe1a698c6d6b8bfd7b0b0e5f4b69f7d69ad49be7dd47038c9ae25.md](../../../../../malware-like/oraculo/downloader/39a1788f1a5fe1a698c6d6b8bfd7b0b0e5f4b69f7d69ad49be7dd47038c9ae25.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `39a1788f1a5fe1a698c6d6b8bfd7b0b0e5f4b69f7d69ad49be7dd47038c9ae25`
- **MD5:** `c5e8cf6dd6df99a80453dc41a708ca73`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.8 |
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
| hash | 39a1788f1a5fe1a698c6d6b8bfd7b0b0e5f4b69f7d69ad49be7dd47038c9ae25 | static_analysis |
| ip | 8.216.8.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
