# 🧬 Payload Analysis

`d46e7bd2bf00f8218fc97badb3d206473bb84bd3552e26caacec43124467d4b0`

## 📌 Resumen

Texto ASCII de 551 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Probe` en `hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery/Probe`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d46e7bd2bf00f8218fc97badb3d206473bb84bd3552e26caacec43124467d4b0.md](../../../../../malware-like/oraculo/downloader/d46e7bd2bf00f8218fc97badb3d206473bb84bd3552e26caacec43124467d4b0.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d46e7bd2bf00f8218fc97badb3d206473bb84bd3552e26caacec43124467d4b0`
- **SHA1:** `49e216566cea0c795a2cdd52876d2ccf24f1edf3`
- **MD5:** `46bd6c8eaa4b5254abb4d88d6023e53a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text |
| Tamaño | 551 B |
| Entropía | 5.18 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery/Probe | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2004/08/addressing | strings |
| url | hxxp://www[.]w3[.]org/2003/05/soap-envelope | strings |
| hash | d46e7bd2bf00f8218fc97badb3d206473bb84bd3552e26caacec43124467d4b0 | static_analysis |
| ip | 204.76.203.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
