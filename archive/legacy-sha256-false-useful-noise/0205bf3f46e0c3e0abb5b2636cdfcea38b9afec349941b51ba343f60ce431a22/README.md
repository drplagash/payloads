# 🧬 Payload Analysis

`0205bf3f46e0c3e0abb5b2636cdfcea38b9afec349941b51ba343f60ce431a22`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `css` en `hxxps://fonts[.]googleapis[.]com/css`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/0205bf3f46e0c3e0abb5b2636cdfcea38b9afec349941b51ba343f60ce431a22.md](../../../../../malware-like/oraculo/downloader/0205bf3f46e0c3e0abb5b2636cdfcea38b9afec349941b51ba343f60ce431a22.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0205bf3f46e0c3e0abb5b2636cdfcea38b9afec349941b51ba343f60ce431a22`
- **SHA1:** `15671c86e0311932803a462c53337f1e38b7436e`
- **MD5:** `2a42bc736435d1ab4da090b934d3f608`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.66 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Open+Sans | strings |
| hash | 0205bf3f46e0c3e0abb5b2636cdfcea38b9afec349941b51ba343f60ce431a22 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
