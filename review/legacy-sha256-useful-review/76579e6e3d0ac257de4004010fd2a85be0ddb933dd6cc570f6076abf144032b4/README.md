# 🧬 Payload Analysis

`76579e6e3d0ac257de4004010fd2a85be0ddb933dd6cc570f6076abf144032b4`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/76579e6e3d0ac257de4004010fd2a85be0ddb933dd6cc570f6076abf144032b4.md](../../../../../malware-like/oraculo/downloader/76579e6e3d0ac257de4004010fd2a85be0ddb933dd6cc570f6076abf144032b4.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `76579e6e3d0ac257de4004010fd2a85be0ddb933dd6cc570f6076abf144032b4`
- **MD5:** `d2c88e11afc66b99ab0ecc4aca3ccd6e`

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
| ip | 190.179.167.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 76579e6e3d0ac257de4004010fd2a85be0ddb933dd6cc570f6076abf144032b4 | static_analysis |
| ip | 47.250.122.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
