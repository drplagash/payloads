# 🧬 Payload Analysis

`204d974c33d5d3c7c57f0dc1189b05a1ce3de55d74cadc7c1fb6b7febe1f368d`

## 📌 Resumen

Texto ASCII de 144 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. **C2 / infraestructura de control:**

- **Posible C2:** `94.154.43.XXX` — confianza Bajo, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/204d974c33d5d3c7c57f0dc1189b05a1ce3de55d74cadc7c1fb6b7febe1f368d.md](../../../../../malware-like/oraculo/downloader/204d974c33d5d3c7c57f0dc1189b05a1ce3de55d74cadc7c1fb6b7febe1f368d.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `204d974c33d5d3c7c57f0dc1189b05a1ce3de55d74cadc7c1fb6b7febe1f368d`
- **SHA1:** `35854188fe4dcd537c7c666d55c3f29e24aa57ce`
- **MD5:** `f88de84efc11f4438addf9e3f82dd12c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 144 B |
| Entropía | 5.14 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
Download indicators (wget/curl + /tmp)
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 94.154.43.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 204d974c33d5d3c7c57f0dc1189b05a1ce3de55d74cadc7c1fb6b7febe1f368d | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
