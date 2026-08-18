# 🧬 Payload Analysis

`1c58cea3f575ab25ef17e0935b60501bd95ea0ffcb030c7e27efa3f1f71ed386`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Infraestructura remota: `hxxps://wordpress[.]org/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/1c58cea3f575ab25ef17e0935b60501bd95ea0ffcb030c7e27efa3f1f71ed386.md](../../../../../malware-like/oraculo/downloader/1c58cea3f575ab25ef17e0935b60501bd95ea0ffcb030c7e27efa3f1f71ed386.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:37:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1c58cea3f575ab25ef17e0935b60501bd95ea0ffcb030c7e27efa3f1f71ed386`
- **MD5:** `bde49c2c4808603d1ac1e2f7d1007860`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.28 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://wordpress[.]org/ | strings |
| hash | 1c58cea3f575ab25ef17e0935b60501bd95ea0ffcb030c7e27efa3f1f71ed386 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
