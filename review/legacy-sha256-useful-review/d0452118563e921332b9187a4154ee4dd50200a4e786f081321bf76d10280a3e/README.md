# 🧬 Payload Analysis

`d0452118563e921332b9187a4154ee4dd50200a4e786f081321bf76d10280a3e`

## 📌 Resumen

Artefacto de 258 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.85. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:47:25.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d0452118563e921332b9187a4154ee4dd50200a4e786f081321bf76d10280a3e`
- **SHA1:** `34282b0ff7977151c733cd7fa92028d5c7f72f2e`
- **MD5:** `750b22d83fa0179e42b4f310f7472bbe`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 258 B |
| Entropía | 4.85 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🖥️ Comandos observados / extraídos

```text
>/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/shm;>/tmp/.x&&cd /
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/shm;>/tmp/.x&&cd / | strings |
| hash | d0452118563e921332b9187a4154ee4dd50200a4e786f081321bf76d10280a3e | static_analysis |
| ip | 60.19.13.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
