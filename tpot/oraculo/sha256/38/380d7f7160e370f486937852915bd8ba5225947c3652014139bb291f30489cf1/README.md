# 🧬 Payload Analysis

`380d7f7160e370f486937852915bd8ba5225947c3652014139bb291f30489cf1`

## 📌 Resumen

Texto ASCII de 622 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `encoding` en `hxxp://schemas[.]xmlsoap[.]org/soap/encoding/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/380d7f7160e370f486937852915bd8ba5225947c3652014139bb291f30489cf1.md](../../../../../malware-like/oraculo/downloader/380d7f7160e370f486937852915bd8ba5225947c3652014139bb291f30489cf1.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `380d7f7160e370f486937852915bd8ba5225947c3652014139bb291f30489cf1`
- **SHA1:** `f7c978617d3925bd0e2dd95f60ba1d5e91788115`
- **MD5:** `626869913929d55a19c90d1e33964201`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (622), with no line terminators |
| Tamaño | 622 B |
| Entropía | 5.37 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (622), with no line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://72.255.3.XXX:37070/Mozi.m | strings |
| ip | 72.255.3.XXX | static_analysis |
| hash | 380d7f7160e370f486937852915bd8ba5225947c3652014139bb291f30489cf1 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
