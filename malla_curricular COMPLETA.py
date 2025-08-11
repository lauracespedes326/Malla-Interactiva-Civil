import streamlit as st
import copy

st.set_page_config(page_title="Malla Interactiva - Ingeniería Civil", layout="wide")

st.markdown("""
<div style='
    background-color: #5CA75C; 
    padding: 20px; 
    border-radius: 10px; 
    text-align: center;
    border: 1px solid #4d924d;
'>
    <h1 style='color: white; margin: 0;'>Malla Curricular - Ingeniería Civil</h1>
</div>
""", unsafe_allow_html=True)


# ----------------- CONFIGURACIÓN -----------------
# Colores
dark_gray = "#e33127"  # Bloqueado en realidad es rojo
blue_selected = "#70A7F8"  # Seleccionado
green_enabled = "#5CA75C"  # Habilitado
sem_colors = ["#DCEFFF", "#CCE5FF", "#B8DAFF", "#A6D1FF", "#94C7FF", "#82BDFF", "#70B3FF", "#5EA9FF"]

# ----------------- MALLA BASE -----------------
base_curriculum = {
    "Semestre 1": [
        {"name": "Cálculo Diferencial", "credits": 3, "prerequisites": [], "corequisites": []},
        {"name": "Álgebra Lineal", "credits": 3, "prerequisites": [], "corequisites": []},
        {"name": "Química de Materiales", "credits": 3, "prerequisites": [], "corequisites": []},
        {"name": "Geometría Descriptiva", "credits": 3, "prerequisites": [], "corequisites": []},
        {"name": "Construcción Sostenible", "credits": 3, "prerequisites": [], "corequisites": []},
        {"name": "Introducción a la Ingeniería", "credits": 2, "prerequisites": [], "corequisites": []}
    ],
    "Semestre 2": [
        {"name": "Cálculo Integral", "credits": 3, "prerequisites": ["Cálculo Diferencial"], "corequisites": []},
        {"name": "Física Mecánica", "credits": 3, "prerequisites": ["Cálculo Diferencial"], "corequisites": []},
        {"name": "Introducción a la Programación", "credits": 3, "prerequisites": [], "corequisites": []},
        {"name": "Geología", "credits": 3, "prerequisites": ["Química de Materiales"], "corequisites": ["Geomática"]},
        {"name": "Geomática", "credits": 3, "prerequisites": ["Geometría Descriptiva"], "corequisites": []},
        {"name": "Proyecto de Diseño en Ingeniería I", "credits": 2, "prerequisites": ["Introducción a la Ingeniería"], "corequisites": []}
    ],
    "Semestre 3": [
        {"name": "Ecuaciones Diferenciales", "credits": 3, "prerequisites": ["Cálculo Integral", "Álgebra Lineal"], "corequisites": []},
        {"name": "Cálculo Vectorial", "credits": 3, "prerequisites": ["Cálculo Integral", "Álgebra Lineal"], "corequisites": []},
        {"name": "Análisis de Amenaza y Confiabilidad en IC", "credits": 3, "prerequisites": ["Cálculo Integral"], "corequisites": []},
        {"name": "Mecánica Estructural I", "credits": 3, "prerequisites": ["Álgebra Lineal", "Física Mecánica", "Cálculo Integral"], "corequisites": []},
        {"name": "Significación Teológica", "credits": 2, "prerequisites": [], "corequisites": ["Proyecto de Diseño en Ingeniería I"]},
        {"name": "Matemática Financiera", "credits": 2, "prerequisites": ["Construcción Sostenible"], "corequisites": []},
        {"name": "Ingeniería de Proyectos I", "credits": 2, "prerequisites": [], "corequisites": ["Matemática Financiera"]}
    ],
    "Semestre 4": [
        {"name": "Métodos Numéricos Aplicados a IC", "credits": 3, "prerequisites": ["Introducción a la Programación", "Ecuaciones Diferenciales"], "corequisites": []},
        {"name": "Mecánica Estructural II", "credits": 3, "prerequisites": ["Mecánica Estructural I", "Cálculo Vectorial", "Ecuaciones Diferenciales"], "corequisites": []},
        {"name": "Mecánica de Suelos", "credits": 4, "prerequisites": ["Análisis de Amenaza y Confiabilidad en IC","Geología"], "corequisites": []},
        {"name": "Transporte y Tránsito", "credits": 4, "prerequisites": [], "corequisites": ["Análisis de Amenaza y Confiabilidad en IC"]},
        {"name": "Proyecto de Diseño en Ingeniería Civil", "credits": 3, "prerequisites": ["Proyecto de Diseño en Ingeniería I", "Ingeniería de Proyectos I"], "corequisites": []}
    ],
    "Semestre 5": [
        {"name": "Mecánica de Fluidos", "credits": 3, "prerequisites": [], "corequisites": ["Mecánica Estructural II"]},
        {"name": "Materiales de Construcción", "credits": 4, "prerequisites": ["Mecánica Estructural I", "Geología"], "corequisites": []},
        {"name": "Diseño Geométrico de Vías", "credits": 2, "prerequisites": ["Transporte y Tránsito"], "corequisites": []},
        {"name": "Mecánica Estructural III", "credits": 4, "prerequisites": ["Métodos Numéricos Aplicados a IC", "Mecánica Estructural II"], "corequisites": []},
        {"name": "Epistemología", "credits": 2, "prerequisites": [], "corequisites": ["Proyecto de Diseño en Ingeniería Civil"]},
        {"name": "Electiva I", "credits": 2, "prerequisites": [], "corequisites": []}
    ],
    "Semestre 6": [
        {"name": "Diseño y Construcción de Estructuras en Concreto Reforzado", "credits": 6, "prerequisites": ["Mecánica Estructural III", "Materiales de Construcción"], "corequisites": []},
        {"name": "Geotecnia Aplicada a Edificaciones", "credits": 4, "prerequisites": ["Mecánica de Suelos"], "corequisites": []},
        {"name": "Geotecnia Aplicada a Obras Lineales", "credits": 4, "prerequisites": ["Mecánica de Suelos"], "corequisites": []},
        {"name": "Proyecto de Diseño Énfasis en Edificaciones", "credits": 6, "prerequisites": ["Proyecto de Diseño en Ingeniería Civil"], "corequisites": ["Diseño y Construcción de Estructuras en Concreto Reforzado", "Geotecnia Aplicada a Edificaciones"]},
        {"name": "Proyecto de Diseño Énfasis en Infraestructura Vial", "credits": 6, "prerequisites": ["Proyecto de Diseño en Ingeniería Civil"], "corequisites": ["Fundamentos de Pavimentos", "Geotecnia Aplicada a Obras Lineales"]},
        {"name": "Proyecto de Diseño Énfasis en Hidrotecnia", "credits": 6, "prerequisites": ["Proyecto de Diseño en Ingeniería Civil"], "corequisites": ["Diseño de Acueductos y Alcantarillado", "Geotecnia Aplicada a Obras Lineales"]}
    ],
    "Semestre 7": [
        {"name": "Hidrología", "credits": 3, "prerequisites": ["Análisis de Amenaza y Confiabilidad en IC"], "corequisites": []},
        {"name": "Hidráulica", "credits": 5, "prerequisites": ["Mecánica de Fluidos", "Métodos Numéricos Aplicados a IC"], "corequisites": ["Hidrología"]},
        {"name": "Fé y Compromiso del Ingeniero", "credits": 2, "prerequisites": [], "corequisites": ["Proyecto de Énfasis"]},
        {"name": "Constitución y Derecho Público", "credits": 2, "prerequisites": ["Proyecto de Diseño I"], "corequisites": []},
        {"name": "Electiva de Enfasis", "credits": 2, "prerequisites": [], "corequisites": []},
        {"name": "Electiva II", "credits": 3, "prerequisites": [], "corequisites": []}
    ],
    "Semestre 8": [
        {"name": "Diseño de Acueductos y Alcantarillado", "credits": 2, "prerequisites": ["Hidráulica"], "corequisites": []},
        {"name": "Proyecto Social Universitario", "credits": 2, "prerequisites": ["Proyecto de Diseño en Ingeniería Civil", "Taller Sentido de Mi Práctica"], "corequisites": []},
        {"name": "Opción Complementaria", "credits": 6, "prerequisites": [], "corequisites": []},
        {"name": "Fundamentos de Pavimentos", "credits": 2, "prerequisites": ["Transporte y Tránsito", "Mecánica de Suelos"], "corequisites": ["Materiales de Construcción"]},
        {"name": "Ética en la Ingeniería", "credits": 2, "prerequisites": ["Proyecto Social Universitario"], "corequisites": []},
        {"name": "Electiva III", "credits": 3, "prerequisites": [], "corequisites": []}
    ]
}

# ----------------- ENFASIS -----------------
enfasis = st.selectbox("Selecciona un énfasis:", ["Edificaciones", "Hidrotecnia", "Infravial"])

curriculum = copy.deepcopy(base_curriculum)
if enfasis == "Edificaciones":
    materias_a_eliminar = ["Geotecnia Aplicada a Obras Lineales","Proyecto de Diseño Énfasis en Infraestructura Vial", "Proyecto de Diseño Énfasis en Hidrotecnia"]
    for sem in curriculum.values():
        sem[:] = [s for s in sem if s["name"] not in materias_a_eliminar]

if enfasis == "Hidrotecnia":
    materias_a_eliminar2 = ["Proyecto de Diseño Énfasis en Infraestructura Vial", "Proyecto de Diseño Énfasis en Edificaciones", "Geotecnia Aplicada a Edificaciones"]
    for sem in curriculum.values():
        sem[:] = [s for s in sem if s["name"] not in materias_a_eliminar2]
        sem[:] = [s for s in sem if s["name"] not in ["Mecánica de Fluidos", "Mecánica de Suelos", "Materiales de Construcción", "Hidrología", "Hidráulica", "Electiva I", "Diseño Geométrico de Vías", "Diseño y Construcción de Estructuras en Concreto Reforzado","Diseño de Acueductos y Alcantarillado", "Fundamentos de Pavimentos"]]
    curriculum["Semestre 4"].append({"name": "Mecánica de Fluidos", "credits": 3, "prerequisites": ["Hidráulica"], "corequisites": []})
    curriculum["Semestre 6"].append({"name": "Diseño de Acueductos y Alcantarillado", "credits": 2, "prerequisites": ["Hidráulica"], "corequisites": []})
    curriculum["Semestre 5"].append({"name": "Mecánica de Suelos", "credits": 3, "prerequisites": ["Materiales de Construcción"], "corequisites": []})
    curriculum["Semestre 5"].append({"name": "Hidrología", "credits": 3, "prerequisites": ["Análisis de Amenaza y Confiabilidad en IC"], "corequisites": []})
    curriculum["Semestre 5"].append({"name": "Hidráulica", "credits": 5, "prerequisites": ["Mecánica de Fluidos", "Métodos Numéricos Aplicados a IC"], "corequisites": ["Hidrología"]})
    curriculum["Semestre 7"].append({"name": "Materiales de Construcción", "credits": 4, "prerequisites": ["Mecánica Estructural I", "Geología"], "corequisites": []})
    curriculum["Semestre 6"].append({"name": "Diseño Geométrico de Vías", "credits": 2, "prerequisites": ["Transporte y Tránsito"], "corequisites": []})
    curriculum["Semestre 8"].append({"name": "Diseño y Construcción de Estructuras en Concreto Reforzado", "credits": 6, "prerequisites": ["Mecánica Estructural III", "Materiales de Construcción"], "corequisites": []})
    curriculum["Semestre 6"].append({"name": "Electiva I", "credits": 2, "prerequisites": [], "corequisites": []})
    curriculum["Semestre 7"].append({"name": "Fundamentos de Pavimentos", "credits": 2, "prerequisites": ["Transporte y Tránsito", "Mecánica de Suelos"], "corequisites": ["Materiales de Construcción"]})

elif enfasis == "Infravial":
    materias_a_eliminar3 = ["Geotecnia Aplicada a Edificaciones","Proyecto de Diseño Énfasis en Hidrotecnia", "Proyecto de Diseño Énfasis en Edificaciones"]
    for sem in curriculum.values():
        sem[:] = [s for s in sem if s["name"] not in materias_a_eliminar3]
        sem[:] = [s for s in sem if s["name"] not in ["Fundamentos de Pavimentos", "Constitución y Derecho Público", "Diseño y Construcción de Estructuras en Concreto Reforzado", "Electiva II", "Electiva III"]]
    curriculum["Semestre 6"].append({"name": "Fundamentos de Pavimentos", "credits": 2, "prerequisites": [], "corequisites": []})
    curriculum["Semestre 6"].append({"name": "Constitución y Derecho Público", "credits": 2, "prerequisites": ["Proyecto de Diseño I"], "corequisites": []})
    curriculum["Semestre 8"].append({"name": "Diseño y Construcción de Estructuras en Concreto Reforzado", "credits": 6, "prerequisites": ["Mecánica Estructural III", "Materiales de Construcción"], "corequisites": []})
    curriculum["Semestre 6"].append({"name": "Electiva II", "credits": 2, "prerequisites": [], "corequisites": []})
    curriculum["Semestre 7"].append({"name": "Electiva III", "credits": 2, "prerequisites": [], "corequisites": []})

# ----------------- FUNCIONES -----------------
subject_lookup = {subject["name"]: subject for sem in curriculum.values() for subject in sem}

if "selected_subjects" not in st.session_state:
    st.session_state.selected_subjects = set()

def can_take(subject):
    return all(prereq in st.session_state.selected_subjects for prereq in subject["prerequisites"])

def missing_coreqs(subject):
    return [coreq for coreq in subject["corequisites"] if coreq not in st.session_state.selected_subjects]

# ----------------- VISUALIZACIÓN -----------------
# ----------------- VISUALIZACIÓN -----------------
# Determinar el número máximo de materias en cualquier semestre
max_materias = max(len(subjects) for subjects in curriculum.values())

# Crear columnas para cada semestre
cols = st.columns(len(curriculum))

# Encabezados de los semestres
for i, (sem, _) in enumerate(curriculum.items()):
    with cols[i]:
        st.markdown(f"<div style='background-color:{sem_colors[i]}; padding:10px; border-radius:10px; text-align:center;'>"
                    f"<h4>{sem}</h4></div>", unsafe_allow_html=True)

# Mostrar las materias por filas (alineadas)
for row in range(max_materias):
    cols = st.columns(len(curriculum))
    for col_idx, (sem, subjects) in enumerate(curriculum.items()):
        with cols[col_idx]:
            if row < len(subjects):
                subj = subjects[row]
                is_selected = subj["name"] in st.session_state.selected_subjects
                habilitada = can_take(subj)
                faltan_coreq = missing_coreqs(subj)

                color = dark_gray
                if is_selected:
                    color = blue_selected
                elif habilitada:
                    color = green_enabled

                label = subj["name"]
                if habilitada and faltan_coreq:
                    label += " ⚠"

                st.markdown(f"<div style='background-color:{color}; padding:10px; border-radius:10px'>",
                            unsafe_allow_html=True)
                if st.checkbox(label, key=f"{sem}_{subj['name']}", value=is_selected):
                    st.session_state.selected_subjects.add(subj["name"])
                else:
                    st.session_state.selected_subjects.discard(subj["name"])

                with st.expander("Requisitos"):
                    st.write(f"*Créditos:* {subj['credits']}")
                    st.write(f"*Prerrequisitos:* {', '.join(subj['prerequisites']) if subj['prerequisites'] else 'Ninguno'}")
                    st.write(f"*Correquisitos:* {', '.join(subj['corequisites']) if subj['corequisites'] else 'Ninguno'}")

                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.write("")  # Espacio vacío para mantener alineación
