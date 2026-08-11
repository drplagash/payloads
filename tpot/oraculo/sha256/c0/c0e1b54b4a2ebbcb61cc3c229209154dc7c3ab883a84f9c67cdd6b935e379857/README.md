# 🧬 Payload Analysis

`c0e1b54b4a2ebbcb61cc3c229209154dc7c3ab883a84f9c67cdd6b935e379857`

## 📌 Resumen

Texto ASCII de 432 B. La evidencia disponible identifica capacidad de descarga remota. Se dispone de 1 comando observado o extraído. **C2 / infraestructura de control:**

- **Posible C2:** `94.154.43.XXX` — confianza Bajo, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/c0e1b54b4a2ebbcb61cc3c229209154dc7c3ab883a84f9c67cdd6b935e379857.md](../../../../../malware-like/oraculo/downloader/c0e1b54b4a2ebbcb61cc3c229209154dc7c3ab883a84f9c67cdd6b935e379857.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c0e1b54b4a2ebbcb61cc3c229209154dc7c3ab883a84f9c67cdd6b935e379857`
- **SHA1:** `a4ac706fd965e3befb2151271654b97e2d3112a4`
- **MD5:** `17f2fd476283afc4da037b64164c1637`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 432 B |
| Entropía | 5.14 |
| Strings | 18 |

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
| hash | c0e1b54b4a2ebbcb61cc3c229209154dc7c3ab883a84f9c67cdd6b935e379857 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
