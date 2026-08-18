# 🧬 Payload Analysis

`3c45da7b8965164b612424ea4c2c268c324d2f6da6373f6c4150f4b0ebb7d56f`

## 📌 Resumen

Texto ASCII de 485 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/3c45da7b8965164b612424ea4c2c268c324d2f6da6373f6c4150f4b0ebb7d56f.md](../../../../../malware-like/oraculo/downloader/3c45da7b8965164b612424ea4c2c268c324d2f6da6373f6c4150f4b0ebb7d56f.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3c45da7b8965164b612424ea4c2c268c324d2f6da6373f6c4150f4b0ebb7d56f`
- **SHA1:** `ca98011b540c4720aa4e2d2e7afc06462b9aa294`
- **MD5:** `a6f85ef11aacf0cc5c1324b0211d74e3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (485), with no line terminators |
| Tamaño | 485 B |
| Entropía | 5.2 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (485), with no line terminators; iocs=6

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://www[.]huawei[.]com/vehicle/nu | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| hash | 3c45da7b8965164b612424ea4c2c268c324d2f6da6373f6c4150f4b0ebb7d56f | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
