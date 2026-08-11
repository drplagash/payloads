# 🧬 Payload Analysis

`786494ddaab0cdbff0aa81bd99f43ff1607aa2d41f4241dde329a3d7cb1cb0d1`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/786494ddaab0cdbff0aa81bd99f43ff1607aa2d41f4241dde329a3d7cb1cb0d1.md](../../../../../malware-like/oraculo/downloader/786494ddaab0cdbff0aa81bd99f43ff1607aa2d41f4241dde329a3d7cb1cb0d1.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `786494ddaab0cdbff0aa81bd99f43ff1607aa2d41f4241dde329a3d7cb1cb0d1`
- **MD5:** `16838c62f47703dc6ff1e3d417c4dea5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.78 |
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
| hash | 786494ddaab0cdbff0aa81bd99f43ff1607aa2d41f4241dde329a3d7cb1cb0d1 | static_analysis |
| ip | 8.211.39.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
