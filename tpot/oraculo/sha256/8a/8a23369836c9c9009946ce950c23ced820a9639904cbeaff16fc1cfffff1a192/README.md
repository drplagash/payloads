# 🧬 Payload Analysis

`8a23369836c9c9009946ce950c23ced820a9639904cbeaff16fc1cfffff1a192`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `no_` en `hxxp://[internal-ip-redacted]/assets/no_`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/8a23369836c9c9009946ce950c23ced820a9639904cbeaff16fc1cfffff1a192.md](../../../../../malware-like/oraculo/downloader/8a23369836c9c9009946ce950c23ced820a9639904cbeaff16fc1cfffff1a192.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8a23369836c9c9009946ce950c23ced820a9639904cbeaff16fc1cfffff1a192`
- **SHA1:** `59cb087e4700a186ae00f486603cc4124b250870`
- **MD5:** `a7498447a576488d0db914dece5d28a1`

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
| url | hxxp://[internal-ip-redacted]/assets/no_ | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | 8a23369836c9c9009946ce950c23ced820a9639904cbeaff16fc1cfffff1a192 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
