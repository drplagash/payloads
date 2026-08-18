# 🧬 Payload Analysis

`98aeca4df27c5f955d766a6ae33c2cf01907e71f8ad9bb0216676c20f62eccab`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `no_` en `hxxp://[internal-ip-redacted]/assets/no_`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/98aeca4df27c5f955d766a6ae33c2cf01907e71f8ad9bb0216676c20f62eccab.md](../../../../../malware-like/oraculo/downloader/98aeca4df27c5f955d766a6ae33c2cf01907e71f8ad9bb0216676c20f62eccab.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `98aeca4df27c5f955d766a6ae33c2cf01907e71f8ad9bb0216676c20f62eccab`
- **SHA1:** `b46be290e2a11774dcfb2088c2428ee756e2fba2`
- **MD5:** `b6e164e8f0ce5dbe6a3a72ecba7bf751`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.66 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/assets/no_ | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | 98aeca4df27c5f955d766a6ae33c2cf01907e71f8ad9bb0216676c20f62eccab | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
