# 🧬 Payload Analysis

`80d7161d5f669d43c3831e091385239ffaf23de6fb28d5eef15e84eaec748c07`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `writing.jpg` en `hxxps://casper[.]ghost[.]org/v1.0.0/images/writing.jpg`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/80d7161d5f669d43c3831e091385239ffaf23de6fb28d5eef15e84eaec748c07.md](../../../../../malware-like/oraculo/downloader/80d7161d5f669d43c3831e091385239ffaf23de6fb28d5eef15e84eaec748c07.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:47.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `80d7161d5f669d43c3831e091385239ffaf23de6fb28d5eef15e84eaec748c07`
- **MD5:** `01a2859c122d1cf92e4fd953a752f41a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.15 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/writing.jpg) | strings |
| hash | 80d7161d5f669d43c3831e091385239ffaf23de6fb28d5eef15e84eaec748c07 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
