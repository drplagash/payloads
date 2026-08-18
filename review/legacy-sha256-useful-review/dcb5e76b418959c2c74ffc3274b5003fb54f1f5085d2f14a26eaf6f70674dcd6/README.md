# 🧬 Payload Analysis

`dcb5e76b418959c2c74ffc3274b5003fb54f1f5085d2f14a26eaf6f70674dcd6`

## 📌 Resumen

Artefacto de 285 B. La evidencia disponible identifica capacidad de descarga remota. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `cd /var/run`
2. `cd /mnt`
3. `cd /usr`
4. `cd /dev`
5. `cd /dev/shm`
6. `cd /` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/dcb5e76b418959c2c74ffc3274b5003fb54f1f5085d2f14a26eaf6f70674dcd6.md](../../../../../malware-like/oraculo/downloader/dcb5e76b418959c2c74ffc3274b5003fb54f1f5085d2f14a26eaf6f70674dcd6.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dcb5e76b418959c2c74ffc3274b5003fb54f1f5085d2f14a26eaf6f70674dcd6`
- **MD5:** `baa936813bd61b8ab1f449f336c290ae`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 285 B |
| Entropía | 4.87 |
| Strings | 7 |

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
| hash | dcb5e76b418959c2c74ffc3274b5003fb54f1f5085d2f14a26eaf6f70674dcd6 | static_analysis |
| ip | 175.107.2.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
