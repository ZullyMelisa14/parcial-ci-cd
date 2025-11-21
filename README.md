# Ejecución Local con nektos/act

## ¿Qué es nektos/act?

`act` es una herramienta que permite ejecutar GitHub Actions workflows **localmente** 
usando contenedores Docker. Simula el entorno de GitHub Actions en tu máquina.

### Ventajas:
- ✅ Prueba workflows antes de hacer push
- ✅ Depuración más rápida
- ✅ Ahorra minutos de CI/CD en GitHub
- ✅ Desarrollo offline

## Requisitos

1. **Docker Desktop** instalado y corriendo
   - [Descargar Docker](https://www.docker.com/products/docker-desktop)

2. **act** instalado:
```bash
   # macOS
   brew install act

   # Windows (con Chocolatey)
   choco install act-cli

   # Linux
   curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```

## Comandos para ejecutar

### Ejecutar el workflow completo:
```bash
act push
```

### Ejecutar solo un job específico:
```bash
act push -j quality-check
```

### Listar workflows disponibles:
```bash
act -l
```

### Ejecutar con verbose para debugging:
```bash
act push -v
```

### Usar imagen específica (más rápida):
```bash
act push -P ubuntu-latest=catthehacker/ubuntu:act-latest
```

## Notas importantes

- La primera ejecución descarga imágenes Docker (~1GB)
- Usa `-n` para dry-run (ver qué haría sin ejecutar)
- Los secrets locales se configuran en `.secrets`
```

### Paso 2: Crear archivo .actrc (opcional)

**`.actrc`**:
```
-P ubuntu-latest=catthehacker/ubuntu:act-latest
--artifact-server-path /tmp/artifacts