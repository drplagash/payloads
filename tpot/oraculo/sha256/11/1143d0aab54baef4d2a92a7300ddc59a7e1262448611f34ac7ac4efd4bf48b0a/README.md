# 🧬 Payload Analysis

`1143d0aab54baef4d2a92a7300ddc59a7e1262448611f34ac7ac4efd4bf48b0a`

## 📌 Resumen

Artefacto de 278 B. La evidencia disponible identifica capacidad de descarga remota. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `cd /var/run`
2. `cd /mnt`
3. `cd /usr`
4. `cd /dev`
5. `cd /dev/shm`
6. `cd /` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/1143d0aab54baef4d2a92a7300ddc59a7e1262448611f34ac7ac4efd4bf48b0a.md](../../../../../malware-like/oraculo/downloader/1143d0aab54baef4d2a92a7300ddc59a7e1262448611f34ac7ac4efd4bf48b0a.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1143d0aab54baef4d2a92a7300ddc59a7e1262448611f34ac7ac4efd4bf48b0a`
- **MD5:** `488e630fa15bdcccfdf32cad30d7cfb5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 278 B |
| Entropía | 4.94 |
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
| hash | 1143d0aab54baef4d2a92a7300ddc59a7e1262448611f34ac7ac4efd4bf48b0a | static_analysis |
| ip | 119.157.76.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
