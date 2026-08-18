# 🧬 Payload Analysis

`65a88c3bbdf66a59d91c6b625a915f238e2ee660ca42ad449c9f16b03ca847da`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `index.php` en `hxxp://[internal-ip-redacted]/index.php`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/65a88c3bbdf66a59d91c6b625a915f238e2ee660ca42ad449c9f16b03ca847da.md](../../../../../malware-like/oraculo/downloader/65a88c3bbdf66a59d91c6b625a915f238e2ee660ca42ad449c9f16b03ca847da.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `65a88c3bbdf66a59d91c6b625a915f238e2ee660ca42ad449c9f16b03ca847da`
- **SHA1:** `0780f4644afb0ed1a38c50b92790cc9be8c2d38e`
- **MD5:** `1e32d6f06196c9a22a1419daa286f14e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.44 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/index.php?title=Main_Page&amp;oldid=1 | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | 65a88c3bbdf66a59d91c6b625a915f238e2ee660ca42ad449c9f16b03ca847da | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
