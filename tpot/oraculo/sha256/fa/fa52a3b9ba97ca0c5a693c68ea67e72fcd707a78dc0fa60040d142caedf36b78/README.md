# 🧬 Payload Analysis

`fa52a3b9ba97ca0c5a693c68ea67e72fcd707a78dc0fa60040d142caedf36b78`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `no_avatar-849f9c04a3a0` en `hxxp://[internal-ip-redacted]/assets/no_avatar-849f9c04a3a0`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/fa52a3b9ba97ca0c5a693c68ea67e72fcd707a78dc0fa60040d142caedf36b78.md](../../../../../malware-like/oraculo/downloader/fa52a3b9ba97ca0c5a693c68ea67e72fcd707a78dc0fa60040d142caedf36b78.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fa52a3b9ba97ca0c5a693c68ea67e72fcd707a78dc0fa60040d142caedf36b78`
- **SHA1:** `bda75eb744b2ced02dde13716a5157f9efd9ecda`
- **MD5:** `a09812315c95f2ebbd2794a9c539a559`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.65 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/assets/no_avatar-849f9c04a3a0 | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | fa52a3b9ba97ca0c5a693c68ea67e72fcd707a78dc0fa60040d142caedf36b78 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
