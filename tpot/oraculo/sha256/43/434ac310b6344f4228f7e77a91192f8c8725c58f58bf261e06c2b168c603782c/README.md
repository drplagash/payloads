# 🧬 Payload Analysis

`434ac310b6344f4228f7e77a91192f8c8725c58f58bf261e06c2b168c603782c`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `11` en `hxxp://gmpg[.]org/xfn/11`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/434ac310b6344f4228f7e77a91192f8c8725c58f58bf261e06c2b168c603782c.md](../../../../../malware-like/oraculo/downloader/434ac310b6344f4228f7e77a91192f8c8725c58f58bf261e06c2b168c603782c.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `434ac310b6344f4228f7e77a91192f8c8725c58f58bf261e06c2b168c603782c`
- **SHA1:** `a8844961b520ab5e195c629c3411f1e2f0650c87`
- **MD5:** `2363b1f6252e91889a68d7e9c48ef0d3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.71 |
| Strings | 13 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://gmpg[.]org/xfn/11 | strings |
| hash | 434ac310b6344f4228f7e77a91192f8c8725c58f58bf261e06c2b168c603782c | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
