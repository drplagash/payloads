# 🧬 Payload Analysis

`2139631c6daa0efd0effad41d79e2efd6fb0f2de15591003eb10c0b4ca0a2f52`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `css` en `hxxps://fonts[.]googleapis[.]com/css`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/2139631c6daa0efd0effad41d79e2efd6fb0f2de15591003eb10c0b4ca0a2f52.md](../../../../../malware-like/oraculo/downloader/2139631c6daa0efd0effad41d79e2efd6fb0f2de15591003eb10c0b4ca0a2f52.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2139631c6daa0efd0effad41d79e2efd6fb0f2de15591003eb10c0b4ca0a2f52`
- **SHA1:** `2cb87b7a7cf1926db85cc1c9b579c15ad73eacc9`
- **MD5:** `4d73897529685ba59a900f6eba7428f1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.72 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Open+Sans | strings |
| hash | 2139631c6daa0efd0effad41d79e2efd6fb0f2de15591003eb10c0b4ca0a2f52 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
