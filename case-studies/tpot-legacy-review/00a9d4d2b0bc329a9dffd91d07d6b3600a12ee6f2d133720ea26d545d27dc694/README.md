# 🧬 Payload Analysis

`00a9d4d2b0bc329a9dffd91d07d6b3600a12ee6f2d133720ea26d545d27dc694`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/00a9d4d2b0bc329a9dffd91d07d6b3600a12ee6f2d133720ea26d545d27dc694.md](../../../../../malware-like/oraculo/downloader/00a9d4d2b0bc329a9dffd91d07d6b3600a12ee6f2d133720ea26d545d27dc694.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `00a9d4d2b0bc329a9dffd91d07d6b3600a12ee6f2d133720ea26d545d27dc694`
- **MD5:** `8c5803e06927e141f4a2f1aaab27504c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.79 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.68.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.68.0 | strings |
| hash | 00a9d4d2b0bc329a9dffd91d07d6b3600a12ee6f2d133720ea26d545d27dc694 | static_analysis |
| ip | 205.210.31.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
