# 🧬 Payload Analysis

`cd10ce1692cd0570b482775e65bf79a865a7719d2606b336dd61c0fcaff9311b`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `ns` en `hxxp://ogp[.]me/ns`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/cd10ce1692cd0570b482775e65bf79a865a7719d2606b336dd61c0fcaff9311b.md](../../../../../malware-like/oraculo/downloader/cd10ce1692cd0570b482775e65bf79a865a7719d2606b336dd61c0fcaff9311b.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cd10ce1692cd0570b482775e65bf79a865a7719d2606b336dd61c0fcaff9311b`
- **SHA1:** `aa5bf7b34de10f8abeab6bdd964c482416faf9f9`
- **MD5:** `e9851ab00a6c217b87ed0cb9df35b85c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.73 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://ogp[.]me/ns# | strings |
| hash | cd10ce1692cd0570b482775e65bf79a865a7719d2606b336dd61c0fcaff9311b | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
