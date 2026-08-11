# 🧬 Payload Analysis

`e1220fb5d6b6860f8e5bfc4f8ab7cf4faae720c65faba23b424267a54d429dce`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Article` en `hxxps://schema[.]org/Article`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/e1220fb5d6b6860f8e5bfc4f8ab7cf4faae720c65faba23b424267a54d429dce.md](../../../../../malware-like/oraculo/downloader/e1220fb5d6b6860f8e5bfc4f8ab7cf4faae720c65faba23b424267a54d429dce.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e1220fb5d6b6860f8e5bfc4f8ab7cf4faae720c65faba23b424267a54d429dce`
- **MD5:** `2fcf971d42f7d1472e707589e0747603`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.3 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://schema[.]org/Article | strings |
| hash | e1220fb5d6b6860f8e5bfc4f8ab7cf4faae720c65faba23b424267a54d429dce | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
