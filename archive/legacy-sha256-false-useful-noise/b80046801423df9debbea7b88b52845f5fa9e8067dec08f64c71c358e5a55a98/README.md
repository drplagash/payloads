# 🧬 Payload Analysis

`b80046801423df9debbea7b88b52845f5fa9e8067dec08f64c71c358e5a55a98`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `welcome.jpg` en `hxxps://casper[.]ghost[.]org/v1.0.0/images/welcome.jpg`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b80046801423df9debbea7b88b52845f5fa9e8067dec08f64c71c358e5a55a98.md](../../../../../malware-like/oraculo/downloader/b80046801423df9debbea7b88b52845f5fa9e8067dec08f64c71c358e5a55a98.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:59:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b80046801423df9debbea7b88b52845f5fa9e8067dec08f64c71c358e5a55a98`
- **SHA1:** `80024308021e309e9f7f13b33d861070bf842b70`
- **MD5:** `5431f6f4bf8cf3afdfb477ea20336eab`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.25 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/welcome.jpg) | strings |
| hash | b80046801423df9debbea7b88b52845f5fa9e8067dec08f64c71c358e5a55a98 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
