# 🧬 Payload Analysis

`db6bc24329ab3b146e7d9614a75bd2f1efbb634a8c1745ae0ac2c1d94962eb4e`

## 📌 Resumen

Artefacto de 1.4 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `xmrig-aarch64-static` en `hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-aarch64-static`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/db6bc24329ab3b146e7d9614a75bd2f1efbb634a8c1745ae0ac2c1d94962eb4e.md](../../../../../malware-like/oraculo/downloader/db6bc24329ab3b146e7d9614a75bd2f1efbb634a8c1745ae0ac2c1d94962eb4e.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `db6bc24329ab3b146e7d9614a75bd2f1efbb634a8c1745ae0ac2c1d94962eb4e`
- **SHA1:** `e6c3423e5e5c88a2291152d6467f93010b40effd`
- **MD5:** `e275a4637fe5da7ae01b46f4a5f3fc79`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 5.51 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://raw[.]githubusercontent[.]com/BenoitDaude/ABCDYUOSD/refs/heads/main/xmrig-aarch64-static | strings |
| url | hxxps://raw[.]githubusercontent[.]co | strings |
| hash | db6bc24329ab3b146e7d9614a75bd2f1efbb634a8c1745ae0ac2c1d94962eb4e | static_analysis |
| ip | 34.24.63.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
