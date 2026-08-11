# 🧬 Payload Analysis

`b73045a7aa1f1ba0868b358a500b33d82e9eb3e8c239205405f846c4aaf9ae1f`

## 📌 Resumen

Artefacto de 273 B. La evidencia disponible identifica capacidad de descarga remota. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `cd /var/run`
2. `cd /mnt`
3. `cd /usr`
4. `cd /dev`
5. `cd /dev/shm`
6. `cd /` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b73045a7aa1f1ba0868b358a500b33d82e9eb3e8c239205405f846c4aaf9ae1f.md](../../../../../malware-like/oraculo/downloader/b73045a7aa1f1ba0868b358a500b33d82e9eb3e8c239205405f846c4aaf9ae1f.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:13.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b73045a7aa1f1ba0868b358a500b33d82e9eb3e8c239205405f846c4aaf9ae1f`
- **MD5:** `42d998b1f330ede93257efa6d4bf70d6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 273 B |
| Entropía | 4.98 |
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
| hash | b73045a7aa1f1ba0868b358a500b33d82e9eb3e8c239205405f846c4aaf9ae1f | static_analysis |
| ip | 182.120.32.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
