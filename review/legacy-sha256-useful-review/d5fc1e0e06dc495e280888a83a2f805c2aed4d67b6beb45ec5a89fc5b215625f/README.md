# 🧬 Payload Analysis

`d5fc1e0e06dc495e280888a83a2f805c2aed4d67b6beb45ec5a89fc5b215625f`

## 📌 Resumen

Artefacto de 275 B. La evidencia disponible identifica capacidad de descarga remota. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `cd /var/run`
2. `cd /mnt`
3. `cd /usr`
4. `cd /dev`
5. `cd /dev/shm`
6. `cd /` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d5fc1e0e06dc495e280888a83a2f805c2aed4d67b6beb45ec5a89fc5b215625f.md](../../../../../malware-like/oraculo/downloader/d5fc1e0e06dc495e280888a83a2f805c2aed4d67b6beb45ec5a89fc5b215625f.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d5fc1e0e06dc495e280888a83a2f805c2aed4d67b6beb45ec5a89fc5b215625f`
- **MD5:** `b93095385a8d9b78c16b2b8cec7827e6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 275 B |
| Entropía | 4.96 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
>/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/shm;>/tmp/.x&&cd /
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/shm;>/tmp/.x&&cd / | strings |
| hash | d5fc1e0e06dc495e280888a83a2f805c2aed4d67b6beb45ec5a89fc5b215625f | static_analysis |
| ip | 223.123.35.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
