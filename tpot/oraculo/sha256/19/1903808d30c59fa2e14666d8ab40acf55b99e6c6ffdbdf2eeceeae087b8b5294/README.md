# 🧬 Payload Analysis

`1903808d30c59fa2e14666d8ab40acf55b99e6c6ffdbdf2eeceeae087b8b5294`

## 📌 Resumen

Texto ASCII de 84 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/1903808d30c59fa2e14666d8ab40acf55b99e6c6ffdbdf2eeceeae087b8b5294.md](../../../../../malware-like/oraculo/downloader/1903808d30c59fa2e14666d8ab40acf55b99e6c6ffdbdf2eeceeae087b8b5294.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1903808d30c59fa2e14666d8ab40acf55b99e6c6ffdbdf2eeceeae087b8b5294`
- **SHA1:** `c991ba8cfe859fc64a0b5391a529536e78a70ed3`
- **MD5:** `aaac5a3b656becebf9f8ae59ae347aa1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
| Entropía | 4.83 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.76.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| command | User-Agent: curl/7.76.1 | strings |
| hash | 1903808d30c59fa2e14666d8ab40acf55b99e6c6ffdbdf2eeceeae087b8b5294 | static_analysis |
| ip | 103.123.227.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
