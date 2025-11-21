# RESPUESTAS - Parcial Calidad de Software Avanzado

**Estudiante:** Zully Melisa Beleño  
**Fecha:** 20 Nov 2025  
**Repositorio:** https://github.com/ZullyMelisa14/parcial-ci-cd.git

---

## PARTE 1 - ESTRATEGIA (15%)

### 1.1 Diferencia entre CI y CD

**Integración Continua (CI):**

La Integración Continua es una práctica de desarrollo donde los desarrolladores 
integran código al repositorio principal frecuentemente (varias veces al día). 
Cada integración dispara un build automatizado que ejecuta:

- Compilación del código
- Pruebas automatizadas (unitarias, integración)
- Análisis estático (linters)
- Validaciones de calidad

**Objetivo principal:** Detectar errores tempranamente, minimizar conflictos de 
integración y mantener el código en un estado funcional constantemente.

**Entrega Continua (CD - Continuous Delivery):**

Extiende CI asegurando que el código siempre esté en un estado desplegable a 
producción. Automatiza el proceso de release, pero el despliegue final a 
producción es manual (requiere aprobación humana).

**Despliegue Continuo (CD - Continuous Deployment):**

Va un paso más allá: cada cambio que pasa todas las etapas del pipeline se 
despliega automáticamente a producción sin intervención humana.

**En este proyecto se implementó CI**, ya que automatizamos integración, testing 
y validación, pero no incluimos despliegue automatizado.

---

### 1.2 Herramientas Seleccionadas

#### Lenguaje: Python 3.11

**Justificación:**
- Sintaxis clara y legible, ideal para demostración educativa
- Ecosistema maduro de herramientas de testing y calidad
- Amplia adopción en industria y academia
- Excelente soporte en GitHub Actions
- Permite enfocarse en conceptos de CI/CD sin complejidad de compilación

#### Linter: flake8 + black

**flake8:**
- Verifica conformidad con PEP 8 (guía de estilo de Python)
- Detecta errores comunes (variables no usadas, imports incorrectos)
- Configurable mediante `.flake8`
- Integración nativa con editores de código

**black:**
- Formateador automático de código
- "The uncompromising code formatter"
- Elimina debates sobre estilo en equipos
- Salida consistente y determinística

**Justificación de usar ambos:**
flake8 detecta problemas, black los previene. La combinación asegura código 
limpio y consistente sin esfuerzo manual.

#### Cobertura: pytest-cov

**Justificación:**
- Integración perfecta con pytest (el framework de testing elegido)
- Reportes en múltiples formatos (terminal, HTML, XML)
- Soporte para coverage.py (estándar de facto en Python)
- Permite configurar umbrales mínimos
- Reportes visuales con líneas exactas no cubiertas

**Alternativas consideradas:**
- coverage.py solo: Menos integrado con pytest
- nose2: Framework menos mantenido

#### Framework de Testing: pytest

**Justificación:**
- Sintaxis simple con asserts nativos de Python
- Fixtures poderosos para setup/teardown
- Parametrización de tests
- Plugins extensivos (pytest-cov, pytest-mock, etc.)
- Mejor salida de errores que unittest

---

### 1.3 Umbral Mínimo de Cobertura

**Umbral seleccionado: 80%**

#### Justificación:

**¿Por qué NO 70%?**
- Demasiado permisivo
- Permite que 30% del código no tenga tests
- En un proyecto pequeño educativo, alcanzar 80% es razonable
- 70% podría ocultar funciones críticas sin probar

**¿Por qué 90%?**
- Balance óptimo entre calidad y pragmatismo
- Asegura que la lógica de negocio esté cubierta
- Permite cierta flexibilidad en código auxiliar
- Estándar de industria para proyectos de calidad media-alta
- Alcanzable en el tiempo del parcial sin sacrificar otras áreas

#### Estrategia de Cobertura:

Priorizar testing de:
1. **Lógica de negocio** (100% cubierta) - ej: operaciones matemáticas
2. **Manejo de errores** (100% cubierta) - ej: división por cero
3. **Funciones públicas** (mínimo 90%)
4. **Código boilerplate** (puede ser ~50%) - ej: `__init__.py`

#### Configuración en `pyproject.toml`:
```toml
[tool.pytest.ini_options]
addopts = "--cov-fail-under=80"
```

Esto hace que pytest falle si la cobertura global es menor a 80%, 
integrándose perfectamente con el pipeline de CI.

---

## ⚙️ PARTE 2 - WORKFLOW CI/CD

### 2.1 Descripción del Workflow

El workflow `ci-quality.yml` implementa un pipeline completo de calidad que:

1. Se activa en push y pull_request a ramas principales
2. Valida calidad de código en múltiples dimensiones
3. Falla rápidamente ante cualquier problema
4. Genera artefactos para análisis posterior

### 2.2 Estructura del Workflow
```yaml
name: CI - Quality Assurance

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]
```

**Justificación:**
- `push` para validar cambios directos
- `pull_request` para validar antes de merge
- Solo en ramas protegidas (main, develop) para optimizar minutos de CI

### 2.3 Pasos del Pipeline

#### Step 1: Checkout
```yaml
- uses: actions/checkout@v4
```

#### Step 2: Setup Python
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'
```
- Instala Python 3.11
- `cache: 'pip'` acelera ejecuciones (cachea dependencias)

#### Step 3: Instalar Dependencias
```yaml
- run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
```
Instala todas las herramientas necesarias.

#### Step 4: Linter (flake8)
```yaml
- run: |
    flake8 src/ tests/ --count --show-source --statistics
```
- `--count`: Muestra total de errores
- `--show-source`: Muestra línea problemática
- `--statistics`: Resume errores por tipo
- **Falla si encuentra violaciones PEP 8**

#### Step 5: Format Check (black)
```yaml
- run: black --check src/ tests/
```
- `--check`: Solo verifica, no modifica
- **Falla si el formato es incorrecto**

#### Step 6: Tests + Coverage
```yaml
- run: |
    pytest tests/ -v \
      --cov=src \
      --cov-report=term-missing \
      --cov-report=xml \
      --cov-fail-under=80
```
- `-v`: Verbose (muestra cada test)
- `--cov=src`: Mide cobertura de carpeta src
- `--cov-report=term-missing`: Muestra líneas no cubiertas en terminal
- `--cov-report=xml`: Genera reporte XML para herramientas externas
- `--cov-fail-under=80`: **Falla si cobertura < 80%**

#### Step 7: Upload Artifacts
```yaml
- uses: actions/upload-artifact@v4
  if: always()
  with:
    name: coverage-report
    path: |
      htmlcov/
      coverage.xml
```
- `if: always()`: Sube incluso si tests fallan (para debugging)
- Permite descargar reportes HTML detallados

### 2.4 Comportamiento ante Fallos

El workflow **se detiene** en el primer error debido al comportamiento por 
defecto de GitHub Actions:

- Si flake8 falla → no ejecuta black, ni tests, ni nada posterior
- Si tests fallan → no sube artefactos (excepto por `if: always()`)
- Exit code != 0 marca el workflow como fallido (❌ rojo)

Esto es intencional: no tiene sentido probar código con errores de sintaxis o 
que no compila.

## 🐳 PARTE 3 - NEKTOS/ACT (15%)

### 3.1 ¿Qué es nektos/act?

**act** es una herramienta CLI que permite ejecutar GitHub Actions workflows 
**localmente** en tu máquina usando contenedores Docker. Esencialmente, simula 
el ambiente de GitHub Actions sin necesidad de hacer push al repositorio.

### 3.2 ¿Cómo funciona?

1. Lee tu archivo `.github/workflows/*.yml`
2. Crea contenedores Docker que imitan los runners de GitHub
3. Ejecuta cada step del workflow dentro de esos contenedores
4. Simula eventos (push, pull_request, etc.)

### 3.3 Ventajas

| Ventaja | Descripción |
|---------|-------------|
| **Desarrollo rápido** | Probar cambios sin esperar push + CI remoto |
| **Debugging eficiente** | Ver logs en tiempo real en tu terminal |
| **Ahorro de minutos CI** | No gasta minutos de GitHub Actions |
| **Trabajo offline** | No requiere internet (después de descargar imágenes) |
| **Iteración rápida** | Ciclo edit-test-fix en segundos |

### 3.4 Requisitos

#### Instalar act

```terminal
choco install act-cli
```
### 3.5 Comandos Principales

#### Listar workflows disponibles
```bash
act -l
```
#### Ejecutar workflow completo
```bash
act push
```
Simula un evento `push` y ejecuta el workflow.


### 3.6 Archivo de Configuración .actrc

Para evitar escribir parámetros cada vez:
```
```
### 3.7 Ejemplo de Ejecución
```bash
$ act push

[CI - Quality Assurance/quality-check] 🚀  Start image=catthehacker/ubuntu:act-latest
[CI - Quality Assurance/quality-check]   🐳  docker pull image=catthehacker/ubuntu:act-latest platform= username= forcePull=false
[CI - Quality Assurance/quality-check]   🐳  docker create image=catthehacker/ubuntu:act-latest platform= entrypoint=["/usr/bin/tail" "-f" "/dev/null"] cmd=[]
[CI - Quality Assurance/quality-check]   🐳  docker run image=catthehacker/ubuntu:act-latest platform= entrypoint=["/usr/bin/tail" "-f" "/dev/null"] cmd=[]
[CI - Quality Assurance/quality-check] ⭐ Run Main Checkout código
[CI - Quality Assurance/quality-check]   🐳  docker cp src=/home/user/parcial-ci-cd/. dst=/home/user/parcial-ci-cd
[CI - Quality Assurance/quality-check]   ✅  Success - Main Checkout código
[CI - Quality Assurance/quality-check] ⭐ Run Main Configurar Python 3.11
...
[CI - Quality Assurance/quality-check]   ✅  Success - Main Ejecutar Linter (flake8)
[CI - Quality Assurance/quality-check]   ✅  Success - Main Verificar formato (black)
[CI - Quality Assurance/quality-check]   ✅  Success - Main Ejecutar pruebas y calcular cobertura
[CI - Quality Assurance/quality-check] 🏁  Job succeeded
```

### 3.9 Troubleshooting

**Problema:** `Error: Cannot connect to the Docker daemon`
```bash
# Solución: Iniciar Docker Desktop
open -a Docker  # Mac
# o abrir Docker Desktop manualmente
```

**Problema:** `Error: Image not found`
```bash
# Solución: Descargar imagen manualmente
docker pull catthehacker/ubuntu:act-latest
```

**Problema:** Workflow falla localmente pero pasa en GitHub
```bash
# Causa común: Diferencias en imágenes
# Solución: Usar imagen más completa
act push -P ubuntu-latest=catthehacker/ubuntu:full-latest
```

---

## 📊 PARTE 4 - VALIDACIÓN Y LOGS (15%)

### 4.1 Identificación de Fallos en Logs

#### 🔍 A) Fallo de Linter (flake8)

**Síntomas:**
- Step "Ejecutar Linter" muestra ❌ rojo
- Exit code: 1
- Salida contiene violaciones específicas

**Cómo identificarlo:**
1. Buscar código de error tipo `E###` o `F###`
2. El número de línea está especificado: `file.py:LINE:COL`
3. El mensaje explica el problema
4. Al final hay un resumen estadístico
5. **Clave:** Exit code 1

**Códigos comunes:**
- `E501`: Línea muy larga
- `E302`: Faltan líneas en blanco
- `F841`: Variable no usada
- `E261`: Falta espacio antes de comentario inline

---

#### 🧪 B) Fallo de Pruebas Unitarias

**Síntomas:**
- Step "Ejecutar pruebas" muestra ❌ rojo
- Se indica qué test falló
- Stack trace completo del error
- Exit code: 1

**Cómo identificarlo:**
1. Buscar palabra `FAILED` en rojo
2. Sección `FAILURES` detalla cada fallo
3. Muestra el assert que falló con `>` al inicio
4. Stack trace indica línea exacta
5. **Resumen final:** `X failed, Y passed`
6. Exit code 1

---

#### 📊 C) Fallo de Cobertura

**Síntomas:**
- Tests pasan (✅ verde)
- PERO el workflow falla
- Mensaje específico sobre cobertura insuficiente
- Exit code: 2 (distinto de tests fallidos)


### 4.2 Comparación: Run Exitoso vs Fallido

#### ✅ RUN EXITOSO

<img width="921" height="663" alt="image" src="https://github.com/user-attachments/assets/b381ae45-2b84-4f7d-a02a-3e438a4a426f" />


#### ❌ RUN FALLIDO

<img width="921" height="530" alt="image" src="https://github.com/user-attachments/assets/3bb903d4-e325-4436-ac8f-e3f2165b7e7d" />
