# 🧬 Payload Analysis

`60273d3db13d47f66d548811f2d01efa443d71bf00478aba4eec0255d88275a5`

## 📌 Resumen

Artefacto de 274 B. La evidencia disponible identifica capacidad de descarga remota. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `cd /var/run`
2. `cd /mnt`
3. `cd /usr`
4. `cd /dev`
5. `cd /dev/shm`
6. `cd /` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/60273d3db13d47f66d548811f2d01efa443d71bf00478aba4eec0255d88275a5.md](../../../../../malware-like/oraculo/downloader/60273d3db13d47f66d548811f2d01efa443d71bf00478aba4eec0255d88275a5.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `60273d3db13d47f66d548811f2d01efa443d71bf00478aba4eec0255d88275a5`
- **MD5:** `3d1823969a777e595e2583efa9d521e2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 274 B |
| Entropía | 4.88 |
| Strings | 5 |

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
| hash | 60273d3db13d47f66d548811f2d01efa443d71bf00478aba4eec0255d88275a5 | static_analysis |
| ip | 110.37.127.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
