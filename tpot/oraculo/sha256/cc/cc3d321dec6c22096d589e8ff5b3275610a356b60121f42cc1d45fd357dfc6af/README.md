# 🧬 Payload Analysis

`cc3d321dec6c22096d589e8ff5b3275610a356b60121f42cc1d45fd357dfc6af`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:08:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cc3d321dec6c22096d589e8ff5b3275610a356b60121f42cc1d45fd357dfc6af`
- **SHA1:** `ffec5e71e3b045110f4ff5f0c7ccf7f8ab9a6048`
- **MD5:** `fb4ca92c4dc5b1f5aa7cf901da0e0541`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.47 |
| Strings | 30 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; high_entropy=7.5; iocs=8

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://crl[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q4.crl0 | strings |
| url | hxxp://crl[.]globalsign[.]com/root-r3.crl0! | strings |
| url | hxxp://ocsp[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q40J | strings |
| url | hxxp://ocsp2[.]globalsign[.]com/rootr30; | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/gsatlasr3dvtlsca2025q4.crt0 | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/root-r3.crt06 | strings |
| url | hxxps://www[.]globalsign[.]com/repository/0 | strings |
| hash | cc3d321dec6c22096d589e8ff5b3275610a356b60121f42cc1d45fd357dfc6af | static_analysis |
| ip | 151.101.130.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
