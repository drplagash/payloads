# 🧬 Payload Analysis

`5bfcea258c294278e243f42525fd479cc0ad6a7c9a1c3227b55a26e570cca70b`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Help:Contents` en `hxxps://www[.]mediawiki[.]org/wiki/Special:MyLanguage/Help:Contents`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/5bfcea258c294278e243f42525fd479cc0ad6a7c9a1c3227b55a26e570cca70b.md](../../../../../malware-like/oraculo/downloader/5bfcea258c294278e243f42525fd479cc0ad6a7c9a1c3227b55a26e570cca70b.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5bfcea258c294278e243f42525fd479cc0ad6a7c9a1c3227b55a26e570cca70b`
- **SHA1:** `d0a86e45968c3da76f27d6ef11d4019de1259849`
- **MD5:** `d2a11323356307d6196181ceac007e97`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.26 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://www[.]mediawiki[.]org/wiki/Special:MyLanguage/Help:Contents | strings |
| hash | 5bfcea258c294278e243f42525fd479cc0ad6a7c9a1c3227b55a26e570cca70b | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
