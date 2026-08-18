# 🧬 Payload Analysis

`630e121db5059e0ecfaddfbcaf53b4ef0a32c1ebf59e59c4a992b71ae722a7f3`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `css` en `hxxps://fonts[.]googleapis[.]com/css`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/630e121db5059e0ecfaddfbcaf53b4ef0a32c1ebf59e59c4a992b71ae722a7f3.md](../../../../../malware-like/oraculo/downloader/630e121db5059e0ecfaddfbcaf53b4ef0a32c1ebf59e59c4a992b71ae722a7f3.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:37:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `630e121db5059e0ecfaddfbcaf53b4ef0a32c1ebf59e59c4a992b71ae722a7f3`
- **MD5:** `066ecb61c08d7283706e478d8d4b999d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.43 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://fonts[.]googleapis[.]com/css?fami | strings |
| hash | 630e121db5059e0ecfaddfbcaf53b4ef0a32c1ebf59e59c4a992b71ae722a7f3 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
