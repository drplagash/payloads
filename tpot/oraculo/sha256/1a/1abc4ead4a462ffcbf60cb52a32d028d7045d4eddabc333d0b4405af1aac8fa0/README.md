# 🧬 Payload Analysis

`1abc4ead4a462ffcbf60cb52a32d028d7045d4eddabc333d0b4405af1aac8fa0`

## 📌 Resumen

Artefacto de 548 B. La evidencia estática disponible identifica capacidad de descarga remota. Se extrajo como destino remoto `hxxp://[internal-ip-redacted]`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:35:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1abc4ead4a462ffcbf60cb52a32d028d7045d4eddabc333d0b4405af1aac8fa0`
- **MD5:** `d801d1babaa16428d1716147a9326ba9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.37 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted] | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | 1abc4ead4a462ffcbf60cb52a32d028d7045d4eddabc333d0b4405af1aac8fa0 | static_analysis |
| ip | 183.105.3.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
