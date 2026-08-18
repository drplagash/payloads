# 🧬 Payload Analysis

`c90b6bdcb56ce9fbcddefd8b5fb4a3bf8513b4420e73b521b6ad402269fe35cd`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `no_` en `hxxp://[internal-ip-redacted]/assets/no_`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/c90b6bdcb56ce9fbcddefd8b5fb4a3bf8513b4420e73b521b6ad402269fe35cd.md](../../../../../malware-like/oraculo/downloader/c90b6bdcb56ce9fbcddefd8b5fb4a3bf8513b4420e73b521b6ad402269fe35cd.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:13.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c90b6bdcb56ce9fbcddefd8b5fb4a3bf8513b4420e73b521b6ad402269fe35cd`
- **MD5:** `48b85e75abf9eb1e669fb8a03e93d0d3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.62 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/assets/no_ | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | c90b6bdcb56ce9fbcddefd8b5fb4a3bf8513b4420e73b521b6ad402269fe35cd | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
