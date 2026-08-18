# 🧬 Payload Analysis

`968a4d733a366b61d507a758a8ee313da3b4c4d86bed97f9dd33874807254753`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `css` en `hxxps://fonts[.]googleapis[.]com/css`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/968a4d733a366b61d507a758a8ee313da3b4c4d86bed97f9dd33874807254753.md](../../../../../malware-like/oraculo/downloader/968a4d733a366b61d507a758a8ee313da3b4c4d86bed97f9dd33874807254753.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:09:37.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `968a4d733a366b61d507a758a8ee313da3b4c4d86bed97f9dd33874807254753`
- **SHA1:** `d3deb6f17762e969d30a7e3f273bd990cb91344f`
- **MD5:** `b9c8159b5640b65394caff63f379009e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.68 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Open+Sans | strings |
| hash | 968a4d733a366b61d507a758a8ee313da3b4c4d86bed97f9dd33874807254753 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
