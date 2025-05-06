from CLASECOLECCION import Coleccion
from CLASEPACIENTE import Paciente
from CLASEPACIENTEAMBULATORIO import PacienteAmbulatorio    
from CLASEPACIENTEHOSPITALIZADO import PacienteHospitalizado

if __name__ == "__main__":
    coleccion = Coleccion()
    coleccion.cargarPacientes()
    opcion = int(input("INGRESE EL NUMERO DE LA OPCION DESEADA: \n 1. Insertar paciente al final de la lista \n 2. Indicar la cantidad de pacientes hospitalizados cuyo diagnostico es neumonía \n 3. Mostrar el importe cobrado por la clínica a todos los pacientes \n 4. Determinar tipo de paciente según una posición en la lista \n 5. Cambiar el valor de consulta \n"))
    while opcion != 0:
        if opcion == 1:
            tipo = int(input("INGRESE EL TIPO DE PACIENTE QUE DESEA REGISTRAR: \n 1. Paciente \n 2. Paciente Ambulatorio con Obra Social \n 3. Paciente Hospitalizado \n"))
            nombre = input("Ingrese el nombre del paciente: \n")
            apellido = input("Ingrese el apellido del paciente: \n")
            email = input("Ingrese el email del paciente: \n")
            telefono = int(input("Ingrese el numero de telefono del paciente: \n"))
            if tipo == 1:
                Npaciente = Paciente(nombre, apellido, email, telefono)
                coleccion.insertarAlFinal(Npaciente)
            elif tipo == 2:
                historialMed = input("Ingrese el historial medico del paciente: \n")
                alergias = input("Ingrese las alergias del paciente: \n")
                obraSocial = input("Ingrese la obra social del paciente: \n")
                Npaciente = PacienteAmbulatorio(nombre, apellido, email, telefono, historialMed, alergias, obraSocial)
                coleccion.insertarAlFinal(Npaciente)
            elif tipo == 3:
                numHab = int(input("Ingrese el numero de habitacion del paciente: \n"))
                fechaIngreso = input("Ingrese la fecha de ingreso del paciente: \n")
                diagnostico = input("Ingrese el diagnostico del paciente: \n")
                cDias = int(input("Ingrese la cantidad de dias de internación: \n"))
                importeDescartables = float(input("Ingrese el importe en concepto de descartables: \n"))
                Npaciente = PacienteHospitalizado(nombre, apellido, email, telefono, numHab, fechaIngreso, diagnostico, cDias, importeDescartables)
                coleccion.insertarAlFinal(Npaciente)
        elif opcion == 2:
            coleccion.contarPacientesNeumonia()
            coleccion.contarPacientesAmbulatorios()
        elif opcion == 3:
            coleccion.mostrarImportes()
        elif opcion == 4:
            try: 
                pos = int(input("Ingrese la posición del paciente que desea consultar: \n"))
                coleccion.determinarTipoPaciente(pos)
            except ValueError:
                print("La posicion debe ser un numero entero \n")
            except IndexError as mensaje:
                print(mensaje)
        elif opcion == 5:
            valor = float(input("Ingrese un nuevo valor de consulta: \n"))
            coleccion.modificarValorConsulta(valor)
        opcion = int(input("INGRESE EL NUMERO DE LA OPCION DESEADA: \n 1. Insertar paciente al final de la lista \n 2. Indicar la cantidad de pacientes hospitalizados cuyo diagnostico es neumonía \n 3. Mostrar el importe cobrado por la clínica a todos los pacientes \n 4. Determinar tipo de paciente según una posición en la lista \n 5. Cambiar el valor de consulta \n"))