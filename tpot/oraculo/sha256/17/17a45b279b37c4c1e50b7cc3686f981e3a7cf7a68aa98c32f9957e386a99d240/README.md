# 🧬 Payload Analysis

`17a45b279b37c4c1e50b7cc3686f981e3a7cf7a68aa98c32f9957e386a99d240`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `ns` en `hxxp://ogp[.]me/ns`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/17a45b279b37c4c1e50b7cc3686f981e3a7cf7a68aa98c32f9957e386a99d240.md](../../../../../malware-like/oraculo/downloader/17a45b279b37c4c1e50b7cc3686f981e3a7cf7a68aa98c32f9957e386a99d240.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `17a45b279b37c4c1e50b7cc3686f981e3a7cf7a68aa98c32f9957e386a99d240`
- **SHA1:** `4e194f386104e7fffea2e83fa337ddec28e905c3`
- **MD5:** `eef7c5067976b4ed85fe13fcc6a96a58`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.62 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://ogp[.]me/ns# | strings |
| hash | 17a45b279b37c4c1e50b7cc3686f981e3a7cf7a68aa98c32f9957e386a99d240 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
