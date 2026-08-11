# 🧬 Payload Analysis

`a510b3ff1c7b01a8803533d9a094645b45587030b801755de73e3a494f234bfa`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Status_404` en `hxxp://[internal-ip-redacted]/Status_404`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/a510b3ff1c7b01a8803533d9a094645b45587030b801755de73e3a494f234bfa.md](../../../../../malware-like/oraculo/downloader/a510b3ff1c7b01a8803533d9a094645b45587030b801755de73e3a494f234bfa.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:28:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a510b3ff1c7b01a8803533d9a094645b45587030b801755de73e3a494f234bfa`
- **SHA1:** `d05d4ee37129c4aa2e6fa05615da8e019f015144`
- **MD5:** `12939f40b6e4433aa620d27c51a560a1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.36 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/Status_404 | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | a510b3ff1c7b01a8803533d9a094645b45587030b801755de73e3a494f234bfa | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
