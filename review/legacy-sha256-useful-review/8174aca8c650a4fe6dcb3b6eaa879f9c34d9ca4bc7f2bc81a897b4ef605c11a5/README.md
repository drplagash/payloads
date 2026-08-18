# 🧬 Payload Analysis

`8174aca8c650a4fe6dcb3b6eaa879f9c34d9ca4bc7f2bc81a897b4ef605c11a5`

## 📌 Resumen

Texto ASCII de 83 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/8174aca8c650a4fe6dcb3b6eaa879f9c34d9ca4bc7f2bc81a897b4ef605c11a5.md](../../../../../malware-like/oraculo/downloader/8174aca8c650a4fe6dcb3b6eaa879f9c34d9ca4bc7f2bc81a897b4ef605c11a5.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8174aca8c650a4fe6dcb3b6eaa879f9c34d9ca4bc7f2bc81a897b4ef605c11a5`
- **MD5:** `531b0a5928d24a319bc47a75c9fc88f3`

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
| ip | 190.179.164.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 8174aca8c650a4fe6dcb3b6eaa879f9c34d9ca4bc7f2bc81a897b4ef605c11a5 | static_analysis |
| ip | 47.84.133.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
