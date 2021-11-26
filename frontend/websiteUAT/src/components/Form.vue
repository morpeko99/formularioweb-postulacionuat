<template>
  <div class="container">
    <b-alert
      :show="dismissCountDownError"
      variant="danger"
      @dismissed="dismissCountDownError=0"
      @dismiss-count-down="countDownChangedError"
    >
      No se pudo agendar su consulta.
    </b-alert>
    <b-alert
      :show="dismissCountDownSuccess"
      variant="success"
      @dismissed="dismissCountDownSuccess=0"
      @dismiss-count-down="countDownChangedSuccess"
    >
       Su consulta fue agendada con éxito.
    </b-alert>
    <div class="row mt-5 justify-content-center">
      <div class="col-sm-9">
        <div class="card">
          <div class="card-header">
            <h3>Agendar Consulta Médica</h3>
          </div>
          <div class="card-body">
            <b-form @submit="onSubmit" class="row g-3">
              <div class="row mt-3 justify-content-center">
                <div class="col-md-4 mt-3">
                  <b-form-group
                    id="input-group-1"
                    label="Nombre:"
                    label-for="input-1"
                  >
                    <b-form-input
                      id="input-1"
                      v-model="form.nombre"
                      type="text"
                      placeholder="Ingrese nombre"
                      :state="nameValidator"
                      trim
                      required
                    ></b-form-input>
                  </b-form-group>
                </div>
                <div class="col-md-4 mt-3">
                  <b-form-group
                    id="input-group-2"
                    label="Apellid Paterno:"
                    label-for="input-2"
                  >
                    <b-form-input
                      id="input-2"
                      v-model="form.apellidoPaterno"
                      placeholder="Ingrese apellido pat."
                      :state="lastname1Validator"
                      trim
                      required
                    ></b-form-input>
                  </b-form-group>
                </div>
                <div class="col-md-4 mt-3">
                  <b-form-group
                    id="input-group-3"
                    label="Apellid Materno:"
                    label-for="input-3"
                  >
                    <b-form-input
                      id="input-3"
                      v-model="form.apellidoMaterno"
                      placeholder="Ingrese apellido mat."
                      :state="lastname2Validator"
                      trim
                      required
                    ></b-form-input>
                  </b-form-group>
                </div>
                <b-form-invalid-feedback :state="nameValidator">
                  Tu nombre solo puede contener letras.
                </b-form-invalid-feedback>
                <b-form-invalid-feedback :state="lastname1Validator">
                  Tu apellido paterno solo puede contener letras.
                </b-form-invalid-feedback>
                <b-form-invalid-feedback :state="lastname2Validator">
                  Tu apellido materno solo puede contener letras.
                </b-form-invalid-feedback>
              </div>
              <div class="row mt-3 justify-content-center">
                <div class="col-md-4 mt-3">
                  <b-form-group
                    id="input-group-4"
                    label="Rut:"
                    label-for="input-4"
                    description="Ejemplo: 12345678-9."
                  >
                    <b-form-input
                      id="input-4"
                      v-model="form.rut"
                      placeholder="Ingrese rut"
                      :state="rutValidator"
                      trim
                      required
                    ></b-form-input>
                  </b-form-group>
                  <b-form-invalid-feedback :state="rutValidator">
                    Ingrese rut sin puntos.
                  </b-form-invalid-feedback>
                  <b-form-valid-feedback :state="rutValidator">
                    Ingresado correctamente.
                  </b-form-valid-feedback>
                </div>
                <div class="col-md-4 mt-3">
                  <b-form-group
                    id="input-group-5"
                    label="Edad:"
                    label-for="input-5"
                  >
                    <b-form-input
                      id="input-5"
                      v-model="form.edad"
                      placeholder="Ingrese edad"
                      :state="yearsValidator"
                      required
                    ></b-form-input>
                  </b-form-group>
                  <b-form-invalid-feedback :state="yearsValidator">
                    Ingrese un número. Debe ser mayor de edad.
                  </b-form-invalid-feedback>
                </div>
                <div class="col-md-4 mt-3">
                  <b-form-group
                    id="input-group-10"
                    label="Sexo:"
                    label-for="input-10"
                  >
                    <b-form-select
                      id="input-10"
                      v-model="form.sexo"
                      :options="sexos"
                      required
                    ></b-form-select>
                  </b-form-group>
                </div>
              </div>

              <div class="col-md-12">
                <b-form-group
                  id="input-group-6"
                  label="Correo:"
                  label-for="input-6"
                >
                  <b-form-input
                    id="input-6"
                    v-model="form.correo"
                    placeholder="Ingrese correo"
                    :state="emailValidator"
                    trim
                    required
                  ></b-form-input>
                </b-form-group>
                <b-form-invalid-feedback :state="emailValidator">
                  Tu correo debe tener la forma "nombre@ejemplo.com".
                </b-form-invalid-feedback>
                <b-form-valid-feedback :state="emailValidator">
                  Ingresado correctamente.
                </b-form-valid-feedback>
              </div>
              <div class="row mt-3 justify-content-center">
                <div class="col-md-4 mt-3">
                  <b-form-group
                    id="input-group-7"
                    label="Día:"
                    label-for="input-7"
                  >
                    <b-form-datepicker
                      id="input-7"
                      size="sm"
                      locale="es"
                      placeholder="Selecciona un día"
                      :date-format-options="{
                        year: 'numeric',
                        month: 'short',
                        day: '2-digit',
                        weekday: 'short',
                      }"
                      v-model="form.fecha"
                      :state="dateValidator"
                      required
                    ></b-form-datepicker>
                  </b-form-group>
                  <b-form-invalid-feedback :state="dateValidator">
                    Debe seleccionar un día posterior al actual.
                  </b-form-invalid-feedback>
                </div>
                <div class="col-md-4 mt-3">
                  <b-form-group
                    id="input-group-8"
                    label="Hora:"
                    label-for="input-8"
                  >
                    <b-form-select
                      id="input-8"
                      v-model="form.hora"
                      :options="horas"
                      required
                    ></b-form-select>
                  </b-form-group>
                </div>
                <div class="col-md-4 mt-3">
                  <b-form-group
                    id="input-group-9"
                    label="Médico:"
                    label-for="input-9"
                  >
                    <b-form-select
                      id="input-9"
                      v-model="form.medico"
                      :options="medicos"
                      required
                    ></b-form-select>
                  </b-form-group>
                </div>
              </div>

              <div class="row mt-4 justify-content-end">
                <div class="col-md-4 text-end">
                  <b-button
                    pill
                    type="submit"
                    variant="success"
                    :disabled="
                      !(
                        nameValidator &&
                        lastname1Validator &&
                        lastname2Validator &&
                        rutValidator &&
                        yearsValidator &&
                        emailValidator &&
                        dateValidator &&
                        selectValidator
                      )
                    "
                    >Agendar</b-button
                  >
                </div>
              </div>
            </b-form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {
  rutValidator,
  emailValidator,
  yearsValidator,
  nameValidator,
  lastname1Validator,
  lastname2Validator,
  dateValidator,
  selectValidator,
} from "../utils/helpers";

export default {
  name: "Form",
  computed: {
    rutValidator,
    emailValidator,
    yearsValidator,
    nameValidator,
    lastname1Validator,
    lastname2Validator,
    dateValidator,
    selectValidator,
  },
  data() {
    return {
      form: {
        nombre: "",
        apellidoPaterno: "",
        apellidoMaterno: "",
        rut: "",
        edad: "",
        sexo: null,
        medico: null,
        fecha: "",
        hora: null,
        correo: "",
      },
      medicos: [
        { text: "Seleccionar médico", value: null },
        "Arturo Vidal",
        "Alexis Sanchez",
        "Benjamin Brereton",
        "Claudio Bravo",
        "Cristian Alvarado",
      ],
      sexos: [
        { text: "Seleccionar sexo", value: null },
        "Femenino",
        "Masculino",
        "Otro",
      ],
      horas: [
        { text: "Seleccionar hora", value: null },
        "09:00",
        "09:30",
        "10:00",
        "11:30",
        "15:00",
      ],
      showErrorAlert: false,
      showSuccessAlert: false,
      dismissSecs: 5,
      dismissCountDownSuccess: 0,
      dismissCountDownError: 0
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      this.createMedicalConsultation(this.form);
    },
    createMedicalConsultation(form) {
      const path = "http://localhost:5000/clients";
      axios
        .post(path, form)
        .then((res) => {
          this.showSuccessAlert_()
          this.resetForm();
        })
        .catch((err) => {
          this.showErrorAlert_()
        });
    },
    resetForm() {
      // Reset our form values
      this.form.nombre = "";
      this.form.apellidoPaterno = "";
      this.form.apellidoMaterno = "";
      this.form.rut = "";
      this.form.edad = "";
      this.form.sexo = null;
      this.form.medico = null;
      this.form.fecha = "";
      this.form.hora = null;
      this.form.correo = "";
    },
    countDownChangedError(dismissCountDown) {
        this.dismissCountDownError = dismissCountDown
    },
    countDownChangedSuccess(dismissCountDown) {
        this.dismissCountDownSuccess = dismissCountDown
    },
    showErrorAlert_() {
      this.dismissCountDownError = this.dismissSecs
    },
    showSuccessAlert_() {
      this.dismissCountDownSuccess = this.dismissSecs
    }
  },
};
</script>

<style scoped>
.custom-select {
  width: 100%;
  padding: 0.375rem 0.75rem;
  color: #212529;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
}
.disabled {
  background-color: rgba(0, 0, 0, 0.03);
  border: 1px solid rgba(0, 0, 0, 0.125);
  color: rgba(0, 0, 0, 0.2);
}
</style>