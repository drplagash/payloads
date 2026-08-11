# 🧬 Payload Analysis

`35e3539a758b144a48a1f6eb6b6eaccd2b5e9f914c67f20fd9f1f0803b65a393`

## 📌 Resumen

Texto ASCII de 710 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/35e3539a758b144a48a1f6eb6b6eaccd2b5e9f914c67f20fd9f1f0803b65a393.md](../../../../../malware-like/oraculo/downloader/35e3539a758b144a48a1f6eb6b6eaccd2b5e9f914c67f20fd9f1f0803b65a393.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `35e3539a758b144a48a1f6eb6b6eaccd2b5e9f914c67f20fd9f1f0803b65a393`
- **SHA1:** `6387528bb232957529c5f756c8f92f188ac3c3ac`
- **MD5:** `c1dc59a055083ff1a0041ff9debb2be5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (710), with no line terminators |
| Tamaño | 710 B |
| Entropía | 5.01 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (710), with no line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| hash | 35e3539a758b144a48a1f6eb6b6eaccd2b5e9f914c67f20fd9f1f0803b65a393 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
