import time
import search # Search methods

####################
tests = (('A', 'B'), ('O', 'E'), ('G', 'Z'), ('N', 'D'), ('M', 'F'))

# ---------------------------------------------------------------------
# Tests normales (obligatorio)
# ---------------------------------------------------------------------

for inicio, objetivo in tests:
    print(f"\n\n--------------- RUTA {inicio}->{objetivo} ---------------\n")
    problem = search.GPSProblem(inicio, objetivo
                       , search.romania)

    print("\n- Búsqueda en amplitud:")
    start_time = time.time()
    result = search.breadth_first_graph_search(problem)
    end_time = time.time()

    tiempo_ejecucion = end_time - start_time
    nodo_sol, generados, visitados, coste_total = result
    print("Ruta: ", nodo_sol.path())
    print("Generados: ", generados)
    print("Visitados: ", visitados)
    print("Coste total: ", coste_total)
    print(f"Tiempo de ejecución: {tiempo_ejecucion}")

    print("\n- Búsqueda en profundidad:")
    start_time = time.time()
    result = search.depth_first_graph_search(problem)
    end_time = time.time()

    tiempo_ejecucion = end_time - start_time
    nodo_sol, generados, visitados, coste_total = result
    print("Ruta: ", nodo_sol.path())
    print("Generados: ", generados)
    print("Visitados: ", visitados)
    print("Coste total: ", coste_total)
    print(f"Tiempo de ejecución: {tiempo_ejecucion}")

    print("\n- Búsqueda ramificación y acotación:")
    start_time = time.time()
    result = search.ramificacion_acotacion(problem)
    end_time = time.time()

    tiempo_ejecucion = end_time - start_time
    nodo_sol, generados, visitados, coste_total = result
    print("Ruta: ", nodo_sol.path())
    print("Generados: ", generados)
    print("Visitados: ", visitados)
    print("Coste total: ", coste_total)
    print(f"Tiempo de ejecución: {tiempo_ejecucion}")

    print("\n- Búsqueda ramificación y acotación con subestimación:")
    start_time = time.time()
    result = search.ramificacion_acotacion_subestimacion(problem)
    end_time = time.time()

    tiempo_ejecucion = end_time - start_time
    nodo_sol, generados, visitados, coste_total = result
    print("Ruta: ", nodo_sol.path())
    print("Generados: ", generados)
    print("Visitados: ", visitados)
    print("Coste total: ", coste_total)
    print(f"Tiempo de ejecución: {tiempo_ejecucion}")


# ---------------------------------------------------------------------
# Demostración heurística con sobreestimación (opcional)
# ---------------------------------------------------------------------

print("\n\n=== DEMOSTRACIÓN: Heurística que sobreestima ===")
print("Objetivo: Ir de Arad (A) a Bucharest (B)")

# 1. Ejecución NORMAL (Heurística Admisible)
# -------------------------------------------
problem_normal = search.GPSProblem('A', 'B', search.romania)

# Nota: search.ramificacion_acotacion_subestimacion devuelve 4 valores
nodo_optimo, generados_opt, visitados_opt, coste_optimo = search.ramificacion_acotacion_subestimacion(problem_normal)

# Obtenemos la ruta legible
ruta_optima = [n.state for n in nodo_optimo.path()]

print(f"\n1. Heurística Admisible (Normal):")
print(f"   Ruta: {ruta_optima}")
print(f"   Coste: {coste_optimo}")


# 2. Ejecución SABOTEADA (Heurística No Admisible)
# ------------------------------------------------
# Usamos la clase que acabamos de crear en search.py
problem_bad = search.GPSProblemOverestimated('A', 'B', search.romania)

nodo_malo, generados_malo, visitados_malo, coste_malo = search.ramificacion_acotacion_subestimacion(problem_bad)

ruta_mala = [n.state for n in nodo_malo.path()]

print(f"\n2. Heurística Sobreestimada (Miente en Sibiu 'S'):")
print(f"   Ruta: {ruta_mala}")
print(f"   Coste: {coste_malo}")


# CONCLUSIÓN
# ----------
print("\n=== CONCLUSIÓN ===")
if coste_malo > coste_optimo:
    print(f"¡DEMOSTRADO! El algoritmo evitó Sibiu ('S') por la sobreestimación.")
    print(f"Coste óptimo: {coste_optimo} vs Coste obtenido: {coste_malo}")
    print("Al no ser admisible la heurística, no se garantiza el camino óptimo.")
else:
    print("No hubo diferencia. Intenta aumentar el valor de retorno en GPSProblemOverestimated.")