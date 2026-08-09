# 🧬 Payload Analysis

`be11d1d76c4b4ea80708c87ced1dfd993331812f40d04ff0154a2d596e8c6be3`

## 📌 Resumen

Artefacto de 548 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `c` en `hxxps://fonts[.]googleapis[.]com/c`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `be11d1d76c4b4ea80708c87ced1dfd993331812f40d04ff0154a2d596e8c6be3`
- **SHA1:** `5fbbcb707d04c54e46f35f14a3f616e3d6ade23f`
- **MD5:** `520ecc4e94cea71c1081e022e390ca6a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.44 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://fonts[.]googleapis[.]com/c | strings |
| hash | be11d1d76c4b4ea80708c87ced1dfd993331812f40d04ff0154a2d596e8c6be3 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
