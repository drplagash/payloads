# 🧬 Payload Analysis

`483d102cbf7b0daf3bb50444500ab9743b1120fe60c12f0d0dd7cff293a8ec31`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/483d102cbf7b0daf3bb50444500ab9743b1120fe60c12f0d0dd7cff293a8ec31.md](../../../../../malware-like/oraculo/downloader/483d102cbf7b0daf3bb50444500ab9743b1120fe60c12f0d0dd7cff293a8ec31.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `483d102cbf7b0daf3bb50444500ab9743b1120fe60c12f0d0dd7cff293a8ec31`
- **MD5:** `c4ccb9bc25c3528c7db344604249f9f0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.81 |
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
| hash | 483d102cbf7b0daf3bb50444500ab9743b1120fe60c12f0d0dd7cff293a8ec31 | static_analysis |
| ip | 47.250.57.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
