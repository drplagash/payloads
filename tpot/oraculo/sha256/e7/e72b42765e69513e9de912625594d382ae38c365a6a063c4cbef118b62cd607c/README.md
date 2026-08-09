# 🧬 Payload Analysis

`e72b42765e69513e9de912625594d382ae38c365a6a063c4cbef118b62cd607c`

## 📌 Resumen

Artefacto de 828 B. Entropía registrada: 5.46. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e72b42765e69513e9de912625594d382ae38c365a6a063c4cbef118b62cd607c`
- **SHA1:** `095858bff445dec7263f23444f5331dd48d22db3`
- **MD5:** `81b9a0a79bdb037d8ae73dac22fe7f0e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 828 B |
| Entropía | 5.46 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
[4lroot@DIR-859:~# >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | [4lroot@DIR-859:~# >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev | strings |
| hash | e72b42765e69513e9de912625594d382ae38c365a6a063c4cbef118b62cd607c | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
