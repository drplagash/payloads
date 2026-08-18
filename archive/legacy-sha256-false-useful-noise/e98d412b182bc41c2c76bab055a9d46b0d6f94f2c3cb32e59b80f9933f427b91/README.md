# 🧬 Payload Analysis

`e98d412b182bc41c2c76bab055a9d46b0d6f94f2c3cb32e59b80f9933f427b91`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Infraestructura remota: `hxxps://api[.]w[.]org/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/e98d412b182bc41c2c76bab055a9d46b0d6f94f2c3cb32e59b80f9933f427b91.md](../../../../../malware-like/oraculo/downloader/e98d412b182bc41c2c76bab055a9d46b0d6f94f2c3cb32e59b80f9933f427b91.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e98d412b182bc41c2c76bab055a9d46b0d6f94f2c3cb32e59b80f9933f427b91`
- **SHA1:** `d0508d4bb841a14decd68ccb043658b4fe8aefdb`
- **MD5:** `e024140656be6b721e63c2dc1352a135`

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
| url | hxxps://api[.]w[.]org/ | strings |
| hash | e98d412b182bc41c2c76bab055a9d46b0d6f94f2c3cb32e59b80f9933f427b91 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
