# 🧬 Payload Analysis

`9238a26164799800bf2bbcde5d0315ca00860de2c242f0299a9d73f9eec3cfe0`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `index.php` en `hxxp://[internal-ip-redacted]/index.php`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/9238a26164799800bf2bbcde5d0315ca00860de2c242f0299a9d73f9eec3cfe0.md](../../../../../malware-like/oraculo/downloader/9238a26164799800bf2bbcde5d0315ca00860de2c242f0299a9d73f9eec3cfe0.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9238a26164799800bf2bbcde5d0315ca00860de2c242f0299a9d73f9eec3cfe0`
- **SHA1:** `248856d8497748933480fcd3bb68881005587d74`
- **MD5:** `8712219bfbaba0ffc3d760652b11881e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.49 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/index.php?title=Main_Page&amp;oldid=1 | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | 9238a26164799800bf2bbcde5d0315ca00860de2c242f0299a9d73f9eec3cfe0 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
